class TelaPagamento:
    def __init__(self, controlador_pagamento):
        self.__controlador_pagamento = controlador_pagamento

    def mostrar_menu(self):
        while True:
            print("\n=== MENU PAGAMENTO ===")
            print("1. Registrar pagamento")
            print("2. Remover pagamento")
            print("3. Alterar pagamento")
            print("4. Listar pagamentos")
            print("0. Voltar")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.cadastrar()
            elif opcao == "2":
                self.remover()
            elif opcao == "3":
                self.alterar()
            elif opcao == "4":
                self.listar()
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")

    def cadastrar(self):
        try:
            index = int(input("Número do atendimento a pagar: ").strip()) - 1
            data = input("Data do pagamento (AAAA-MM-DD): ").strip()
            valor_pago = float(input("Valor pago (R$): ").strip())
            print("Tipo de pagamento: 1. Dinheiro  2. PIX  3. Cartão de crédito")
            tipo_opcao = input("Escolha: ").strip()

            cpf_pagador = numero_cartao = bandeira_cartao = None

            if tipo_opcao == "1":
                tipo = "dinheiro"
            elif tipo_opcao == "2":
                tipo = "pix"
                cpf_pagador = input("CPF do pagador (somente números): ").strip()
            elif tipo_opcao == "3":
                tipo = "cartao"
                numero_cartao = input("Número do cartão (16 dígitos): ").strip()
                bandeira_cartao = input("Bandeira do cartão: ").strip()
            else:
                raise ValueError("Tipo de pagamento inválido.")

            self.__controlador_pagamento.cadastrar(
                tipo, data, valor_pago, index,
                cpf_pagador, numero_cartao, bandeira_cartao
            )
            print("Pagamento registrado com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def remover(self):
        try:
            self.listar()
            index = int(input("Número do pagamento a remover: ").strip()) - 1
            self.__controlador_pagamento.remover(index)
            print("Pagamento removido com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def alterar(self):
        try:
            self.listar()
            index = int(input("Número do pagamento a alterar: ").strip()) - 1
            print("Deixe em branco para manter o valor atual.")
            data = input("Nova data (AAAA-MM-DD): ").strip() or None
            valor_str = input("Novo valor pago (R$): ").strip()
            valor_pago = float(valor_str) if valor_str else None
            self.__controlador_pagamento.alterar(index, data, valor_pago)
            print("Pagamento alterado com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def listar(self):
        try:
            pagamentos = self.__controlador_pagamento.listar()
            print("\n=== PAGAMENTOS ===")
            for i, p in enumerate(pagamentos):
                print(f"{i+1}. Data: {p.data} | Valor pago: R${p.valor_pago:.2f} | Tipo: {type(p).__name__}")
        except ValueError as e:
            print(f"Erro: {e}")