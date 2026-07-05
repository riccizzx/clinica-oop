from model.paciente import Paciente
from Exceptions.pacienteException import PacienteException
from datetime import date

class ControladorPaciente:
    def __init__(self):
        self.__pacientes = []
        
    def cadastrar(self, nome, celular, cpf, data_nascimento, nome_responsavel=None, cpf_responsavel=None):
        for p in self.__pacientes:
            if p.cpf == cpf:
                raise PacienteException(f"Já existe um paciente com o CPF {cpf}.")
        
        paciente = Paciente(nome, celular, cpf, data_nascimento)
        if not paciente.validar_cpf():
            raise PacienteException("CPF inválido.")
            
        if paciente.verificar_idade():
            if not nome_responsavel or not cpf_responsavel:
                raise PacienteException("Paciente menor de idade precisa de responsável.")
            paciente.nome_responsavel = nome_responsavel
            paciente.cpf_responsavel = cpf_responsavel
            
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
            raise PacienteException("Nenhum paciente cadastrado.")
        
        return [
            {
                "nome": p.nome,
                "celular": p.celular,
                "cpf": p.cpf,
                "data_nascimento": p.data_nascimento,
                "nome_responsavel": p.nome_responsavel,
                "cpf_responsavel": p.cpf_responsavel
            }
            for p in self.__pacientes
        ]
    
    def buscar_por_cpf(self, cpf):
        for p in self.__pacientes:
            if p.cpf == cpf:
                return p
        raise PacienteException(f"Paciente com CPF {cpf} não encontrado.")
