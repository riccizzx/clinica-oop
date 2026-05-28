
from abc import ABC, abstractmethod
from pessoa import Pessoa


class Profissional(Pessoa):
    def __init__(self, nome, celular, cpf, especialidade):
        super().__init__(nome, celular, cpf)
        self.__especialidade = especialidade
    
    @property
    def especialidade(self):
        return self.__especialidade
        
    @especialidade.setter
    def especialidade(self, especialidade):
        self.__especialidade = especialidade

    # abaixo vão os métodos;