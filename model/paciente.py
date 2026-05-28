
from abc import ABC, abstractmethod
from .pessoa import Pessoa
from pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, data_nascimento, nome_responsavel = None, celular_responsavel = None):
        super().__init__(data_nascimento)
        self.__nome_responsavel = nome_responsavel
        self.__celular_responsavel = celular_responsavel

    
    # abaixo vão os métodos;