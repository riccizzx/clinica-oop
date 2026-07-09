from model.pagamentoDinheiro import PagamentoDinheiro
from model.pagamentoPix import PagamentoPix
from model.pagamentoCartao import PagamentoCartao
from Exceptions.pagamentoException import PagamentoException

class ControladorPagamento:
    def __init__(self, controlador_atendimento):
        self.__registros = []
        self.__controlador_atendimento = controlador_atendimento

    def cadastrar(self, tipo, data, valor_pago, index_atendimento, cpf_pagador=None, numero_cartao=None, bandeira_cartao=None):
        atendimento = self.__controlador_atendimento.buscar(index_atendimento)

        if atendimento.verificar_pagamento_pendente() is False:
            raise PagamentoException("Este atendimento já está totalmente pago.")
        if data > atendimento.data:
            raise PagamentoException("Pagamento não pode ser realizado após a data do atendimento.")

        if tipo == "dinheiro":
            pagamento = PagamentoDinheiro(data, valor_pago)
        elif tipo == "pix":
            if not cpf_pagador:
                raise PagamentoException("CPF do pagador é obrigatório para pagamento via PIX.")
            pagamento = PagamentoPix(data, valor_pago, cpf_pagador)
        elif tipo == "cartao":
            if not numero_cartao or not bandeira_cartao:
                raise PagamentoException("Número e bandeira do cartão são obrigatórios para pagamento via cartão.")
            pagamento = PagamentoCartao(data, valor_pago, numero_cartao, bandeira_cartao)
        else:
            raise PagamentoException("Tipo de pagamento inválido. Use: dinheiro, pix ou cartao.")

        if not pagamento.validar_pagamento(atendimento):
            raise PagamentoException("Pagamento inválido. Verifique os dados informados.")

        atendimento.adicionar_pagamento(pagamento)
        self.__registros.append((pagamento, atendimento))
        return pagamento

    def remover(self, index):
        if index < 0 or index >= len(self.__registros):
            raise PagamentoException("Pagamento não encontrado.")
        pagamento, atendimento = self.__registros.pop(index)
        atendimento.remover_pagamento(pagamento)

    def alterar(self, index, data=None, valor_pago=None):
        pagamento = self.buscar(index)
        if data:
            pagamento.data = data
        if valor_pago is not None:
            pagamento.valor_pago = valor_pago

    def listar(self):
        if not self.__registros:
            raise PagamentoException("Nenhum pagamento registrado.")

        return [
            {
                "data": p.data,
                "valor_pago": p.valor_pago,
                "tipo": type(p).__name__
            }
            for p, _ in self.__registros
        ]

    def buscar(self, index):
        if index < 0 or index >= len(self.__registros):
            raise PagamentoException("Pagamento não encontrado.")
        return self.__registros[index][0]
