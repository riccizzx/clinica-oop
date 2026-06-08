class ControladorProfissional:
    def init(self):
        self.profissionais = []

    def cadastrar(self, profissional):
        for p in self.profissionais:
            if p.cpf == profissional.cpf:
                raise ValueError(f"Já existe um profissional com o CPF {profissional.cpf}.")
        if not profissional.validar_cpf():
            raise ValueError("CPF inválido.")
        if not profissional.validar_registro():
            raise ValueError("Registro profissional inválido.")
        self.profissionais.append(profissional)

    def remover(self, cpf):
        profissional = self.buscar_por_cpf(cpf)
        self.profissionais.remove(profissional)

    def alterar(self, cpf, nome=None, celular=None, especialidade=None, registro_profissional=None):
        profissional = self.buscar_por_cpf(cpf)
        if nome:
            profissional.nome = nome
        if celular:
            profissional.celular = celular
        if especialidade:
            profissional.especialidade = especialidade
        if registro_profissional:
            profissional.registro_profissional = registro_profissional

    def listar(self):
        if not self.profissionais:
            raise ValueError("Nenhum profissional cadastrado.")
        return list(self.profissionais)

    def buscar_por_cpf(self, cpf):
        for p in self.__profissionais:
            if p.cpf == cpf:
                return p
        raise ValueError(f"Profissional com CPF {cpf} não encontrado.")