class TelaProcedimento:
    def __init__(self, controlador_procedimento):
        self.__controlador_procedimento = controlador_procedimento

    def mostrar_menu(self):
        while True:
            print("\n=== MENU PROCEDIMENTO ===")
            print("1. Registrar procedimento")
            print("2. Remover procedimento")
            print("3. Alterar procedimento")
            print("4. Listar procedimentos")
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
            descricao = input("Descrição do procedimento: ").strip()
            custo = float(input("Custo (R$): ").strip())
            cpf_profissional = input("CPF do profissional responsável: ").strip()
            index = int(input("Número do atendimento vinculado: ").strip()) - 1
            self.__controlador_procedimento.cadastrar(descricao, custo, cpf_profissional, index)
            print("Procedimento registrado com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def remover(self):
        try:
            self.listar()
            index = int(input("Número do procedimento a remover: ").strip()) - 1
            self.__controlador_procedimento.remover(index)
            print("Procedimento removido com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def alterar(self):
        try:
            self.listar()
            index = int(input("Número do procedimento a alterar: ").strip()) - 1
            print("Deixe em branco para manter o valor atual.")
            descricao = input("Nova descrição: ").strip() or None
            custo_str = input("Novo custo (R$): ").strip()
            custo = float(custo_str) if custo_str else None
            cpf_profissional = input("Novo CPF do profissional responsável: ").strip() or None
            self.__controlador_procedimento.alterar(index, descricao, custo, cpf_profissional)
            print("Procedimento alterado com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def listar(self):
        try:
            procedimentos = self.__controlador_procedimento.listar()
            print("\n=== PROCEDIMENTOS ===")
            for i, p in enumerate(procedimentos):
                print(f"{i+1}. {p.descricao} | Custo: R${p.calcular_custo():.2f} | Profissional: {p.profissional_responsavel.nome}")
        except ValueError as e:
            print(f"Erro: {e}")