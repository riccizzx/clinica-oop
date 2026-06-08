from model.tipo_atendimento import TipoAtendimento


class TelaTipoAtendimento:
    def init(self, controlador_tipo_atendimento):
        self.controlador_tipo_atendimento = controlador_tipo_atendimento

    def mostrar_menu(self):
        while True:
            print("\n=== MENU TIPO DE ATENDIMENTO ===")
            print("1. Cadastrar tipo de atendimento")
            print("2. Remover tipo de atendimento")
            print("3. Alterar tipo de atendimento")
            print("4. Listar tipos de atendimento")
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
            nome = input("Nome do tipo: ").strip()
            descricao = input("Descrição: ").strip()
            valor_base = float(input("Valor base (R$): ").strip())
            tipo = TipoAtendimento(nome, descricao, valor_base)
            self.controlador_tipo_atendimento.cadastrar(tipo)
            print("Tipo de atendimento cadastrado com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def remover(self):
        try:
            nome = input("Nome do tipo a remover: ").strip()
            self.__controlador_tipo_atendimento.remover(nome)
            print("Tipo de atendimento removido com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")
    def alterar(self):
        try:
            nome = input("Nome do tipo a alterar: ").strip()
            print("Deixe em branco para manter o valor atual.")
            novo_nome = input("Novo nome: ").strip() or None
            descricao = input("Nova descrição: ").strip() or None
            valor_str = input("Novo valor base (R$): ").strip()
            valor_base = float(valor_str) if valor_str else None
            self.controlador_tipo_atendimento.alterar(nome, novo_nome, descricao, valor_base)
            print("Tipo de atendimento alterado com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def listar(self):
        try:
            tipos = self.controlador_tipo_atendimento.listar()
            print("\n=== TIPOS DE ATENDIMENTO ===")
            for i, t in enumerate(tipos):
                print(f"{i+1}. {t.nome} | Descrição: {t.descricao} | Valor base: R${t.valor_base:.2f}")
        except ValueError as e:
            print(f"Erro: {e}")