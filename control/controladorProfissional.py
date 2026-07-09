from model.profissional import Profissional
from Exceptions.profissionalException import ProfissionalException

class ControladorProfissional:
    def __init__(self):
        self.__profissionais = []

    def cadastrar(self, nome, celular, cpf, especialidade, registro_profissional):
        for p in self.__profissionais:
            if p.cpf == cpf:
                raise ProfissionalException(f"Já existe um profissional com o CPF {cpf}.")
        
        profissional = Profissional(nome, celular, cpf, especialidade, registro_profissional)
        
        if not profissional.validar_cpf():
            raise ProfissionalException("CPF inválido.")
        if not profissional.validar_registro():
            raise ProfissionalException("Registro profissional inválido.")
            
        self.__profissionais.append(profissional)

    def remover(self, cpf):
        profissional = self.buscar_por_cpf(cpf)
        self.__profissionais.remove(profissional)

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
        if not self.__profissionais:
            raise ProfissionalException("Nenhum profissional cadastrado.")
        
        return [
            {
                "nome": p.nome,
                "celular": p.celular,
                "cpf": p.cpf,
                "especialidade": p.especialidade,
                "registro_profissional": p.registro_profissional
            }
            for p in self.__profissionais
        ]

    def buscar_por_cpf(self, cpf):
        for p in self.__profissionais:
            if p.cpf == cpf:
                return p
        raise ProfissionalException(f"Profissional com CPF {cpf} não encontrado.")
