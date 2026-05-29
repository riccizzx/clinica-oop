
from abc import ABC, abstractmethod
#from .pessoa import Pessoa
from model.pessoa import Pessoa
from model.procedimento import Procedimento
from model.atendimento import Atendimento

class Paciente(Pessoa):
    def __init__(self, data_nascimento, nome_responsavel = None, celular_responsavel = None):
        super().__init__(data_nascimento)
        self.__nome_responsavel = nome_responsavel
        self.__celular_responsavel = celular_responsavel

    
    # abaixo vão os métodos;    
    def verificar_idade(self):
        idade = self.calcular_idade(self.data_nascimento)
        if idade < 18:
            return True
        else:
            return False
        
    def verificar_responsavel(self):
        if self.verificar_idade():
            if self.__nome_responsavel is not None and self.__celular_responsavel is not None:
                return True
            else:
                return False
        else:
            return True