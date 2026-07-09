from model.atendimento import Atendimento
from Exceptions.atendimentoException import AtendimentoException

class ControladorAtendimento:
    def __init__(self, controlador_paciente, controlador_clinica, controlador_profissional, controlador_tipo_atendimento):
        self.__atendimentos = []
        self.__controlador_paciente = controlador_paciente
        self.__controlador_clinica = controlador_clinica
        self.__controlador_profissional = controlador_profissional
        self.__controlador_tipo_atendimento = controlador_tipo_atendimento

    def cadastrar(self, data, horario_inicio, horario_fim, nome_clinica, cidade_clinica, cpf_paciente, cpf_profissional, nome_tipo, valor=None):
        clinica = self.__controlador_clinica.buscar(nome_clinica, cidade_clinica)
        paciente = self.__controlador_paciente.buscar_por_cpf(cpf_paciente)
        profissional = self.__controlador_profissional.buscar_por_cpf(cpf_profissional)
        tipo = self.__controlador_tipo_atendimento.buscar(nome_tipo)

        if not clinica.validar_horario_atendimento(horario_inicio, horario_fim):
            raise AtendimentoException("Horário fora do funcionamento da clínica.")
        if paciente.verificar_idade() and not paciente.verificar_resp():
            raise AtendimentoException("Paciente menor de idade sem responsável cadastrado.")

        if valor is None:
            valor = tipo.valor_base
        if valor < 0:
            raise AtendimentoException("Valor do atendimento inválido.")

        atendimento = Atendimento(data, horario_inicio, horario_fim, valor, clinica, paciente, profissional, tipo)
        self.__atendimentos.append(atendimento)
        return atendimento

    def remover(self, index):
        if index < 0 or index >= len(self.__atendimentos):
            raise AtendimentoException("Atendimento não encontrado.")
        self.__atendimentos.pop(index)

    def cancelar(self, index):
        # Cancela o atendimento (mantém o registro no histórico, mas marca como cancelado)
        atendimento = self.buscar(index)
        atendimento.cancelar()

    def reagendar(self, index):
        # Reativa um atendimento cancelado, voltando-o para o status "agendado"
        atendimento = self.buscar(index)
        atendimento.agendar()

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
            raise AtendimentoException("Nenhum atendimento registrado.")
        
        return [
            {
                "data": a.data,
                "horario_inicio": a.horario_inicio,
                "horario_fim": a.horario_fim,
                "tipo_atendimento": a.tipo_atendimento.nome,
                "paciente": a.paciente.nome,
                "profissional": a.profissional.nome,
                "clinica": a.clinica.nome,
                "status": a.status,
                "valor_total": a.calcular_valor_total(),
                "valor_restante": a.calcular_valor_restante()
            }
            for a in self.__atendimentos
        ]

    def buscar(self, index):
        if index < 0 or index >= len(self.__atendimentos):
            raise AtendimentoException("Atendimento não encontrado.")
        return self.__atendimentos[index]

    def relatorio_clinicas_mais_atendimentos(self):
        atendimentos_validos = [a for a in self.__atendimentos if not a.esta_cancelado()]
        if not atendimentos_validos:
            raise AtendimentoException("Nenhum atendimento registrado.")
        contagem = {}
        for a in atendimentos_validos:
            chave = f"{a.clinica.nome} - {a.clinica.cidade}"
            contagem[chave] = contagem.get(chave, 0) + 1
        return sorted(contagem.items(), key=lambda x: x[1], reverse=True)

    def relatorio_atendimentos_mais_caros_baratos(self):
        atendimentos_validos = [a for a in self.__atendimentos if not a.esta_cancelado()]
        if not atendimentos_validos:
            raise AtendimentoException("Nenhum atendimento registrado.")
        ordenados = sorted(atendimentos_validos, key=lambda a: a.calcular_valor_total(), reverse=True)
        # We need to return primitives/dicts here for the view
        mais_caros = [
            {"data": a.data, "paciente": a.paciente.nome, "valor_total": a.calcular_valor_total()} for a in ordenados[:3]
        ]
        mais_baratos = [
            {"data": a.data, "paciente": a.paciente.nome, "valor_total": a.calcular_valor_total()} for a in ordenados[-3:]
        ]
        return {
            "mais_caros": mais_caros,
            "mais_baratos": mais_baratos
        }
