
"""



"""
#from __future__ import annotations
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.pagamento import Pagamento

#from model.pagamento import Pagamento
from model.paciente import Paciente
from model.profissional import Profissional
from model.procedimento import Procedimento
from model.tipo_atendimento import TipoAtendimento

class Atendimento:
    def __init__(self, data, horario_inicio, horario_fim, valor):
        self.__data = data
        self.__horario_inicio = horario_inicio
        self.__horario_fim = horario_fim
        self.__valor = valor
        self.__procedimentos: list[Procedimento] = []
        self.__pagamentos: list[Pagamento] = []

    @property
    def data(self):
        return self.__data
    
    @property
    def horario_inicio(self):
        return self.__horario_inicio
    
    @property
    def horario_fim(self):
        return self.__horario_fim
    
    @property
    def valor(self):
        return self.__valor
    
    @data.setter
    def data(self, data):
        self.__data = data

    @horario_inicio.setter
    def horario_inicio(self, horario_inicio):
        self.__horario_inicio = horario_inicio

    @horario_fim.setter
    def horario_fim(self, horario_fim):
        self.__horario_fim = horario_fim

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    # metodos;
    def agendar(self, tipo_atendimento: TipoAtendimento, paciente: Paciente,
                 profissional: Profissional, horario_inicio, horario_fim):
        pass

    def cancelar(self, tipo_atendimento: TipoAtendimento, paciente: Paciente,
                  profissional: Profissional, horario_inicio, horario_fim):
        pass

    def validar_horario(self) -> bool:
        try:
            return self.__horario_inicio < self.__horario_fim
        except Exception:
            return False
        
    def adicionar_procedimento(self, procedimento: Procedimento):
        # lista de procedimentos, onde cada procedimento tem um custo, e o valor do atendimento é atualizado com base no custo do procedimento e no valor base do tipo de atendimento.
        pass

    def adicionar_pagamento(self, pagamento: Pagamento):
        # 
        pass

    def calcular_valor_total(self):
        pass

    def calcular_valor_restante(self):
        pass

    def verificar_pagamento_restante(self):
        pass