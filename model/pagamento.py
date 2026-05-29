

"""
    Estou pensando na idea de implementar uma classe abstrata para pagamento, pois existe 3 tipos diferentes 
    de pagamento, e cada um tem suas peculiaridades, como por exemplo,

    as funções vao ser implementadas com base na variavel tipo_pagamento que pode ser "dinheiro", "cartao_credito" ou 
    "cartao_debito", e cada função vai ter uma lógica diferente para cada tipo de pagamento.

    """
from __future__ import annotations # import para evitar problemas de importação em loop, pois a classe Pagamento vai precisar importar a classe Atendimento,
# e a classe Atendimento vai precisar importar a classe Pagamento, e isso pode causar um erro de importação em loop, então com esse import, isso é evitado.
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model.atendimento import Atendimento

class Pagamento(ABC):
    def __init__(
        self,
        data: str,
        valor_pago: float,
        tipo_pagamento: str,
        cpf_pagador: str,
        numero_cartao: str = None,
    ):
        self.__data = data
        self.__valor_pago = valor_pago
        self.__tipo_pagamento = tipo_pagamento
        self.__cpf_pagador = cpf_pagador
        self.__numero_cartao = numero_cartao
    
    # abaixo vão os métodos;
    """
        na implemetação do método realizar_pagamento, a lógica vai ser diferente para cada tipo de pagamento, por exemplo,
        se o tipo de pagamento for "dinheiro", o método vai verificar se o valor pago
    """

    @property
    def data(self):
        return self.__data

    @property
    def valor_pago(self):
        return self.__valor_pago

    @property
    def tipo_pagamento(self):
        return self.__tipo_pagamento

    @property
    def cpf_pagador(self):
        return self.__cpf_pagador

    @property
    def numero_cartao(self):
        return self.__numero_cartao

    @data.setter
    def data(self, data: str):
        self.__data = data

    @valor_pago.setter
    def valor_pago(self, valor_pago: float):
        self.__valor_pago = valor_pago

    @tipo_pagamento.setter
    def tipo_pagamento(self, tipo_pagamento: str):
        self.__tipo_pagamento = tipo_pagamento

    @cpf_pagador.setter
    def cpf_pagador(self, cpf_pagador: str):
        self.__cpf_pagador = cpf_pagador

    @numero_cartao.setter
    def numero_cartao(self, numero_cartao: str):
        self.__numero_cartao = numero_cartao

    @abstractmethod
    def realizar_pagamento(self, atendimento: Atendimento):
        pass

    @abstractmethod
    def validar_pagamento(self, atendimento: Atendimento) -> bool:
        pass

    @abstractmethod
    def calcular_saldo(self, atendimento: Atendimento) -> float:
        pass
