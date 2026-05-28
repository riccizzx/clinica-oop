

"""
    Estou pensando na idea de implementar uma classe abstrata para pagamento, pois existe 3 tipos diferentes 
    de pagamento, e cada um tem suas peculiaridades, como por exemplo,

    as funções vao ser implementadas com base na variavel tipo_pagamento que pode ser "dinheiro", "cartao_credito" ou 
    "cartao_debito", e cada função vai ter uma lógica diferente para cada tipo de pagamento.

    """

from abc import ABC, abstractmethod
from .atendimento import Atendimento

class Pagamento(ABC):
    def __init__(self, data, valor, tipo_pagamento, cpf_pagador, numero_cartao=None):
        self.__data = data
        self.__valor = valor  
        self.__tipo_pagamento = tipo_pagamento
        self.__cpf_pagador = cpf_pagador
        self.__numero_cartao = numero_cartao
    
    # abaixo vão os métodos;
    """
        na implemetação do método realizar_pagamento, a lógica vai ser diferente para cada tipo de pagamento, por exemplo,
        se o tipo de pagamento for "dinheiro", o método vai verificar se o valor pago
    
    """
    @abstractmethod
    def realizar_pagamento(self, atendimento: Atendimento):
        pass

    @abstractmethod
    def validar_pagamento(self, atendimento: Atendimento):
        pass

    @abstractmethod
    def calcular_saldo(self, atendimento: Atendimento):
        pass