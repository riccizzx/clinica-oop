from model.procedimento import Procedimento
from Exceptions.procedimentoException import ProcedimentoException

class ControladorProcedimento:
    def __init__(self, controlador_profissional, controlador_atendimento):
        self.__registros = []
        self.__controlador_profissional = controlador_profissional
        self.__controlador_atendimento = controlador_atendimento

    def cadastrar(self, descricao, custo, cpf_profissional, index_atendimento):
        profissional = self.__controlador_profissional.buscar_por_cpf(cpf_profissional)
        atendimento = self.__controlador_atendimento.buscar(index_atendimento)
        if atendimento.esta_cancelado():
            raise ProcedimentoException("Não é possível registrar procedimento em um atendimento cancelado.")
        procedimento = Procedimento(descricao, custo, profissional)
        atendimento.adicionar_procedimento(procedimento)
        self.__registros.append((procedimento, atendimento))
        return procedimento

    def remover(self, index):
        if index < 0 or index >= len(self.__registros):
            raise ProcedimentoException(f"Índice de procedimento inválido: {index}")
        procedimento, atendimento = self.__registros.pop(index)
        atendimento.remover_procedimento(procedimento)

    def alterar(self, index, descricao=None, custo=None, cpf_profissional=None):
        procedimento = self.buscar(index)
        if descricao:
            procedimento.descricao = descricao
        if custo is not None:
            if custo < 0:
                raise ProcedimentoException("Custo inválido")
            procedimento.custo = custo
        if cpf_profissional:
            profissional = self.__controlador_profissional.buscar_por_cpf(cpf_profissional)
            procedimento.profissional_responsavel = profissional

    def listar(self):
        if not self.__registros:
            raise ProcedimentoException("Nenhum procedimento registrado.")

        return [
            {
                "descricao": p.descricao,
                "custo": p.calcular_custo(),
                "profissional": p.profissional_responsavel.nome
            }
            for p, _ in self.__registros
        ]

    def buscar(self, index):
        if index < 0 or index >= len(self.__registros):
            raise ProcedimentoException(f"Índice de procedimento inválido: {index}")
        return self.__registros[index][0]

    def relatorio_mais_populares(self):
        if not self.__registros:
            raise ProcedimentoException("Nenhum procedimento registrado.")
        contagem = {}
        for p, _ in self.__registros:
            contagem[p.descricao] = contagem.get(p.descricao, 0) + 1
        return sorted(contagem.items(), key=lambda x: x[1], reverse=True)

    def relatorio_mais_caros_baratos(self):
        if not self.__registros:
            raise ProcedimentoException("Nenhum procedimento registrado.")
        ordenados = sorted((p for p, _ in self.__registros), key=lambda p: p.calcular_custo(), reverse=True)
        mais_caros = [
            {"descricao": p.descricao, "custo": p.calcular_custo()} for p in ordenados[:3]
        ]
        mais_baratos = [
            {"descricao": p.descricao, "custo": p.calcular_custo()} for p in ordenados[-3:]
        ]
        return {
            "mais_caros": mais_caros,
            "mais_baratos": mais_baratos
        }
