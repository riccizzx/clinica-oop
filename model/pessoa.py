from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome: str, celular: str, cpf: str):
        self.__nome = nome
        self.__celular = celular
        self.__cpf = cpf

    # nome
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    # celular
    @property
    def celular(self):
        return self.__celular
    
    @celular.setter
    def celular(self, celular: str):
        self.__celular = celular

    # cpf
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

    # Métodos
    
    @abstractmethod
    def validar_cpf(self) -> bool:
        pass
