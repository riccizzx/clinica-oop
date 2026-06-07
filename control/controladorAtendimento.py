from model.atendimento import Atendimento

class ControladorAtendimento:
    def __init__(self, controlador_paciente, controlador_clinica, controlador_profissional, controlador_tipo_atendimento):
        self.__atendimentos = []
        self.__controlador_paciente = controlador_paciente
        self.__controlador_clinica = controlador_clinica
        self.__controlador_profissional = controlador_profissional
        self.__controlador_tipo_atendimento = controlador_tipo_atendimento

    def cadastrar(self, data, horario_inicio, horario_fim, valor, nome_clinica, cidade_clinica, cpf_paciente, cpf_profissional, nome_tipo):
        clinica = self.__controlador_clinica.buscar(nome_clinica, cidade_clinica)
        paciente = self.__controlador_paciente.buscar_por_cpf(cpf_paciente)
        profissional = self.__controlador_profissional.buscar_por_cpf(cpf_profissional)
        tipo = self.__controlador_tipo_atendimento.buscar(nome_tipo)

        if not clinica.validar_horario_atendimento(horario_inicio, horario_fim):
            raise ValueError("Horário fora do funcionamento da clínica.")
        if paciente.verificar_idade() and not paciente.verificar_resp():
            raise ValueError("Paciente menor de idade sem responsável cadastrado.")

        atendimento = Atendimento(data, horario_inicio, horario_fim, valor, clinica, paciente, profissional, tipo)
        self.__atendimentos.append(atendimento)
        return atendimento

    def remover(self, index):
        if index < 0 or index >= len(self.__atendimentos):
            raise ValueError("Atendimento não encontrado.")
        self.__atendimentos.pop(index)

    def alterar(self, index, data=None, horario_inicio=None, horario_fim=None, valor=None):
        atendimento = self.buscar(index)
        if data:
            atendimento.data = data
        if horario_inicio:
            atendimento.horario_inicio = horario_inicio
        if horario_fim:
            atendimento.horario_fim = horario_fim
        if valor:
            atendimento.valor = valor

    def listar(self):
        if not self.__atendimentos:
            raise ValueError("Nenhum atendimento registrado.")
        return list(self.__atendimentos)

    def buscar(self, index):
        if index < 0 or index >= len(self.__atendimentos):
            raise ValueError("Atendimento não encontrado.")
        return self.__atendimentos[index]

    def relatorio_clinicas_mais_atendimentos(self):
        if not self.__atendimentos:
            raise ValueError("Nenhum atendimento registrado.")
        contagem = {}
        for a in self.__atendimentos:
            chave = f"{a.clinica.nome} - {a.clinica.cidade}"
            contagem[chave] = contagem.get(chave, 0) + 1
        return sorted(contagem.items(), key=lambda x: x[1], reverse=True)

    def relatorio_atendimentos_mais_caros_baratos(self):
        if not self.__atendimentos:
            raise ValueError("Nenhum atendimento registrado.")
        ordenados = sorted(self.__atendimentos, key=lambda a: a.calcular_valor_total(), reverse=True)
        return {
            "mais_caros": ordenados[:3],
            "mais_baratos": ordenados[-3:]
        }
