class ControladorPaciente:
    def __init__(self):
        self.__pacientes = []
        
    def cadastrar(self, paciente):
        for p in self.__pacientes:
            if p.cpf == paciente.cpf:
                raise ValueError(f"Já existe um paciente com o CPF {paciente.cpf}.")
        if not paciente.validar_cpf():
            raise ValueError("CPF inválido.")
        if not paciente.verificar_resp():
            raise ValueError("Paciente menor de idade precisa de responsável.")
        self.__pacientes.append(paciente)
    
    def remover(self, cpf):
        paciente = self.buscar_por_cpf(cpf)
        self.__pacientes.remove(paciente)
        
    def alterar(self, cpf, nome=None, celular=None, nome_responsavel=None, cpf_responsavel=None):
        paciente = self.buscar_por_cpf(cpf)
        if nome:
            paciente.nome = nome
        if celular:
            paciente.celular = celular
        if nome_responsavel:
            paciente.nome_responsavel = nome_responsavel
        if cpf_responsavel:
            paciente.cpf_responsavel = cpf_responsavel
    
    def listar(self):
        if not self.__pacientes:
            raise ValueError("Nenhum paciente cadastrado.")
        return list(self.__pacientes)
    
    def buscar_por_cpf(self, cpf):
        for p in self.__pacientes:
            if p.cpf == cpf:
                return p
        raise ValueError(f"Paciente com CPF {cpf} não encontrado.")
