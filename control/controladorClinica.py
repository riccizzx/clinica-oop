class ControladorClinica:
    def __init__(self):
        self.__clinicas = []

    def cadastrar(self, clinica):
        for c in self.__clinicas:
            if c.nome == clinica.nome and c.cidade == clinica.cidade:
                raise ValueError(f"Já existe uma clínica com o nome '{clinica.nome}' em {clinica.cidade}.")
        self.__clinicas.append(clinica)

    def remover(self, nome, cidade):
        clinica = self.buscar(nome, cidade)
        self.__clinicas.remove(clinica)

    def alterar(self, nome, cidade, novo_nome=None, nova_cidade=None, horario_abertura=None, horario_fechamento=None):
        clinica = self.buscar(nome, cidade)
        if novo_nome:
            clinica.nome = novo_nome
        if nova_cidade:
            clinica.cidade = nova_cidade
        if horario_abertura:
            clinica.horario_abertura = horario_abertura
        if horario_fechamento:
            clinica.horario_fechamento = horario_fechamento

    def listar(self):
        if not self.__clinicas:
            raise ValueError("Nenhuma clínica cadastrada.")
        return list(self.__clinicas)

    def buscar(self, nome, cidade):
        for c in self.__clinicas:
            if c.nome == nome and c.cidade == cidade:
                return c
        raise ValueError(f"Clínica '{nome}' em {cidade} não encontrada.")
