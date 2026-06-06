from datetime import date
from model.pessoa import Pessoa


class Paciente(Pessoa):
    def __init__(self,
        nome: str,
        celular: str,
        cpf: str,
        data_nascimento: date,
        nome_responsavel: str = None,
        cpf_responsavel: str = None,
    ):
        super().__init__(nome, celular, cpf)
        self.__data_nascimento = data_nascimento
        self.__nome_responsavel = nome_responsavel
        self.__cpf_responsavel = cpf_responsavel

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @property
    def nome_responsavel(self):
        return self.__nome_responsavel

    @property
    def cpf_responsavel(self):
        return self.__cpf_responsavel

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: date):
        self.__data_nascimento = data_nascimento

    @nome_responsavel.setter
    def nome_responsavel(self, nome_responsavel: str):
        self.__nome_responsavel = nome_responsavel

    @cpf_responsavel.setter
    def cpf_responsavel(self, cpf_responsavel: str):
        self.__cpf_responsavel = cpf_responsavel

    def validar_cpf(self) -> bool:
        return len(self.cpf) == 11 and self.cpf.isdigit()

    def verificar_idade(self) -> bool:
        return self.calcular_idade(self.__data_nascimento) < 18

    def verificar_resp(self) -> bool:
        if self.verificar_idade():
            return (
                self.__nome_responsavel is not None
                and self.__cpf_responsavel is not None
            )
        return True