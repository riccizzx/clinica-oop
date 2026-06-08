from model.pagamentoDinheiro import PagamentoDinheiro
from model.pagamentoPix import PagamentoPix
from model.pagamentoCartao import PagamentoCartao


class ControladorPagamento:
    def init(self, controlador_atendimento):
        self.pagamentos = []
        self.controlador_atendimento = controlador_atendimento

    def cadastrar(self, tipo, data, valor_pago, index_atendimento, cpf_pagador=None, numero_cartao=None, bandeira_cartao=None):
        atendimento = self.controlador_atendimento.buscar(index_atendimento)

        if atendimento.verificar_pagamento_pendente() is False:
            raise ValueError("Este atendimento já está totalmente pago.")
        if data > atendimento.data:
            raise ValueError("Pagamento não pode ser realizado após a data do atendimento.")

        if tipo == "dinheiro":
            pagamento = PagamentoDinheiro(data, valor_pago)
        elif tipo == "pix":
            if not cpf_pagador:
                raise ValueError("CPF do pagador é obrigatório para pagamento via PIX.")
            pagamento = PagamentoPix(data, valor_pago, cpf_pagador)
        elif tipo == "cartao":
            if not numero_cartao or not bandeira_cartao:
                raise ValueError("Número e bandeira do cartão são obrigatórios para pagamento via cartão.")
            pagamento = PagamentoCartao(data, valor_pago, numero_cartao, bandeira_cartao)
        else:
            raise ValueError("Tipo de pagamento inválido. Use: dinheiro, pix ou cartao.")

        if not pagamento.validar_pagamento(atendimento):
            raise ValueError("Pagamento inválido. Verifique os dados informados.")

        atendimento.adicionar_pagamento(pagamento)
        self.pagamentos.append(pagamento)
        return pagamento
    def remover(self, index):
        if index < 0 or index >= len(self.pagamentos):
            raise ValueError("Pagamento não encontrado.")
        self.pagamentos.pop(index)

    def alterar(self, index, data=None, valor_pago=None):
        pagamento = self.buscar(index)
        if data:
            pagamento.data = data
        if valor_pago is not None:
            pagamento.valor_pago = valor_pago

    def listar(self):
        if not self.pagamentos:
            raise ValueError("Nenhum pagamento registrado.")
        return list(self.pagamentos)

    def buscar(self, index):
        if index < 0 or index >= len(self.pagamentos):
            raise ValueError("Pagamento não encontrado.")
        return self.pagamentos[index]