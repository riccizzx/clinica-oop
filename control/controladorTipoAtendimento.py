class ControladorTipoAtendimento:
    def __init__(self):
        self.__tipos = []

    def cadastrar(self, tipo):
        for t in self.__tipos:
            if t.nome == tipo.nome:
                raise ValueError(f"Já existe um tipo de atendimento com o nome '{tipo.nome}'.")
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
            raise ValueError("Nenhum tipo de atendimento cadastrado.")
        return list(self.__tipos)

    def buscar(self, nome):
        for t in self.__tipos:
            if t.nome == nome:
                return t
        raise ValueError(f"Tipo de atendimento '{nome}' não encontrado.")