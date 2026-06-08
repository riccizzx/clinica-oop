from model.procedimento import Procedimento

class ControladorProcedimento:
    def init(self, controlador_profissional, controlador_atendimento):
        self.procedimentos = []
        self.controlador_profissional = controlador_profissional
        self.controlador_atendimento = controlador_atendimento

    def cadastrar(self, descricao, custo, cpf_profissional, index_atendimento):
        profissional = self.controlador_profissional.buscar_por_cpf(cpf_profissional)
        atendimento = self.controlador_atendimento.buscar(index_atendimento)
        procedimento = Procedimento(descricao, custo, profissional)
        atendimento.adicionar_procedimento(procedimento)
        self.procedimentos.append(procedimento)
        return procedimento

    def remover(self, index):
        if index < 0 or index >= len(self.procedimentos):
            raise ValueError("Procedimento não encontrado.")
        self.procedimentos.pop(index)

    def alterar(self, index, descricao=None, custo=None, cpf_profissional=None):
        procedimento = self.buscar(index)
        if descricao:
            procedimento.descricao = descricao
        if custo is not None:
            procedimento.custo = custo
        if cpf_profissional:
            profissional = self.controlador_profissional.buscar_por_cpf(cpf_profissional)
            procedimento.profissional_responsavel = profissional

    def listar(self):
        if not self.procedimentos:
            raise ValueError("Nenhum procedimento registrado.")
        return list(self.procedimentos)

    def buscar(self, index):
        if index < 0 or index >= len(self.procedimentos):
            raise ValueError("Procedimento não encontrado.")
        return self.__procedimentos[index]
    def relatorio_mais_populares(self):
        if not self.procedimentos:
            raise ValueError("Nenhum procedimento registrado.")
        contagem = {}
        for p in self.procedimentos:
            contagem[p.descricao] = contagem.get(p.descricao, 0) + 1
        return sorted(contagem.items(), key=lambda x: x[1], reverse=True)

    def relatorio_mais_caros_baratos(self):
        if not self.procedimentos:
            raise ValueError("Nenhum procedimento registrado.")
        ordenados = sorted(self.procedimentos, key=lambda p: p.calcular_custo(), reverse=True)
        return {
            "mais_caros": ordenados[:3],
            "mais_baratos": ordenados[-3:]
        }