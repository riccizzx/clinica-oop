
# aqui sera a implementação do controlador do sistema, onde serão implementados os métodos para realizar as operações do sistema, como cadastrar paciente, cadastrar atendimento, realizar pagamento, etc.

from model.pagamentoCartao import PagamentoCartao
from model.pagamentoDinheiro import PagamentoDinheiro
from model.pagamentoPix import PagamentoPix

class ControladorSistema:
    def __init__(self):
        self.pacientes = []
        self.atendimentos = []
        self.pagamentos = []

    def cadastrar_paciente(self, nome, cpf, telefone):
        paciente = {
            "nome": nome,
            "cpf": cpf,
            "telefone": telefone
        }
        self.pacientes.append(paciente)
        return paciente

    def cadastrar_atendimento(self, paciente_cpf, valor_total):
        atendimento = {
            "paciente_cpf": paciente_cpf,
            "valor_total": valor_total
        }
        self.atendimentos.append(atendimento)
        return atendimento

    def realizar_pagamento(self, tipo_pagamento, data, valor_pago, cpf_pagador, numero_cartao=None):
        if tipo_pagamento == "dinheiro":
            pagamento = PagamentoDinheiro(data, valor_pago, cpf_pagador)
        elif tipo_pagamento == "pix":
            pagamento = PagamentoPix(data, valor_pago, cpf_pagador)
        elif tipo_pagamento == "cartao":
            pagamento = PagamentoCartao(data, valor_pago, tipo_pagamento, cpf_pagador, numero_cartao)
        else:
            raise ValueError("Tipo de pagamento inválido")
        
        self.pagamentos.append(pagamento)
        return pagamento