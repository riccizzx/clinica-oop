
from abc import abstractmethod

from model.pagamento import Pagamento

class PagamentoCartao(Pagamento):
    def __init__(self,data: str,valor_pago: float,tipo_pagamento: str,cpf_pagador: str,numero_cartao: str):
        super().__init__(data, valor_pago, tipo_pagamento, cpf_pagador, numero_cartao)

    """
    implementação dos métodos abstratos da classe pagamento
    """

    @property
    def numero_cartao(self):
        return self.__numero_cartao
    
    @numero_cartao.setter
    def numero_cartao(self, numero_cartao: str):
        self.__numero_cartao = numero_cartao

    def validar_cartao(self) -> bool:
        if (self.numero_cartao != None and len(self.numero_cartao) == 16 and self.numero_cartao.isdigit()):
            return True
        return False

    def realizar_pagamento(self, atendimento) -> bool:
        """Realiza o pagamento com cartão se for válido"""
        if self.validar_cartao():
            return True
        return False
    
    def validar_pagamento(self, atendimento) -> bool:
        """Valida se o cartão está correto"""
        return self.validar_cartao()
    
    def calcular_saldo(self, atendimento) -> float:
        """Calcula o saldo após o pagamento"""
        valor_total = atendimento.valor_total if hasattr(atendimento, 'valor_total') else 0
        return valor_total - self.valor_pago