
from tipo_atendimento import TipoAtendimento

class Procedimento:
    def __init__(self, descricao, custo):
        self.__descricao = descricao   
        self.__custo = custo   

    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def custo(self):
        return self.__custo
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @custo.setter
    def custo(self, custo):
        self.__custo = custo

    # metodos;
    def calcular_custo_total(self, tipo_atendimento):
        return self.__custo + tipo_atendimento.valor_base