from model.tipo_atendimento import TipoAtendimento
from Exceptions.tipoAtendimentoException import TipoAtendimentoException

class ControladorTipoAtendimento:
    def __init__(self):
        self.__tipos = []

    def cadastrar(self, nome, descricao, valor_base):
        for t in self.__tipos:
            if t.nome == nome:
                raise TipoAtendimentoException(f"Já existe um tipo de atendimento com o nome '{nome}'.")
        
        tipo = TipoAtendimento(nome, descricao, valor_base)
        self.__tipos.append(tipo)

    def remover(self, nome):
        tipo = self.buscar(nome)
        self.__tipos.remove(tipo)

    def alterar(self, nome, novo_nome=None, descricao=None, valor_base=None):
        tipo = self.buscar(nome)
        if novo_nome:
            tipo.nome = novo_nome
        if descricao:
            tipo.descricao = descricao
        if valor_base is not None:
            tipo.atualizar_valor_base(valor_base)

    def listar(self):
        if not self.__tipos:
            raise TipoAtendimentoException("Nenhum tipo de atendimento cadastrado.")
        
        return [
            {
                "nome": t.nome,
                "descricao": t.descricao,
                "valor_base": t.valor_base
            }
            for t in self.__tipos
        ]

    def buscar(self, nome):
        for t in self.__tipos:
            if t.nome == nome:
                return t
        raise TipoAtendimentoException(f"Tipo de atendimento '{nome}' não encontrado.")