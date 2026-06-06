
from model.pagamento import Pagamento
from model.atendimento import Atendimento

class PagamentoDinheiro(Pagamento):
    def __init__(self, data, valor_pago, cpf_pagador):
        super().__init__(data="", valor_pago=0.0, tipo_pagamento="dinheiro", cpf_pagador="")
        self.__data = data
        self.__valor_pago = valor_pago
        self.__cpf_pagador = cpf_pagador

    @property
    def data(self):
        return self.__data
    
    @property
    def valor_pago(self):
        return self.__valor_pago
    
    @property
    def cpf_pagador(self):
        return self.__cpf_pagador
    
    @data.setter
    def data(self, data):
        self.__data = data

    @valor_pago.setter
    def valor_pago(self, valor_pago):
        self.__valor_pago = valor_pago

    @cpf_pagador.setter
    def cpf_pagador(self, cpf_pagador):
        self.__cpf_pagador = cpf_pagador

    def realizar_pagamento(self, atendimento) -> bool:
        """Realiza o pagamento em dinheiro se o valor for suficiente"""
        if self.validar_pagamento(atendimento):
            return True
        return False

    def validar_pagamento(self, atendimento) -> bool:
        """Valida se o valor pago é suficiente para cobrir o atendimento"""
        valor_total = atendimento.valor_total
        if self.valor_pago >= valor_total:
            return True
        return False

    def calcular_saldo(self, atendimento) -> float:
        """Calcula o saldo/troco após o pagamento"""
        valor_total = atendimento.valor_total
        return self.valor_pago - valor_total
    
