class TelaRelatorios:
    def __init__(self, controlador_atendimento, controlador_procedimento):
        self.__controlador_atendimento = controlador_atendimento
        self.__controlador_procedimento = controlador_procedimento

    def mostrar_menu(self):
        while True:
            print("\n=== MENU RELATÓRIOS ===")
            print("1. Clínicas com maior número de atendimentos")
            print("2. Atendimentos mais caros e mais baratos")
            print("3. Procedimentos mais realizados")
            print("4. Procedimentos mais caros e mais baratos")
            print("0. Voltar")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.clinicas_mais_atendimentos()
            elif opcao == "2":
                self.atendimentos_mais_caros_baratos()
            elif opcao == "3":
                self.procedimentos_mais_populares()
            elif opcao == "4":
                self.procedimentos_mais_caros_baratos()
            elif opcao == "0":
                break
            else:
                print("Opção inválida.")

    def clinicas_mais_atendimentos(self):
        try:
            ranking = self.__controlador_atendimento.relatorio_clinicas_mais_atendimentos()
            print("\n=== CLÍNICAS COM MAIS ATENDIMENTOS ===")
            for i, (clinica, qtd) in enumerate(ranking):
                print(f"{i+1}. {clinica} | Atendimentos: {qtd}")
        except ValueError as e:
            print(f"Erro: {e}")

    def atendimentos_mais_caros_baratos(self):
        try:
            resultado = self.__controlador_atendimento.relatorio_atendimentos_mais_caros_baratos()
            print("\n=== ATENDIMENTOS MAIS CAROS ===")
            for a in resultado["mais_caros"]:
                print(f"  {a.data} | {a.paciente.nome} | R${a.calcular_valor_total():.2f}")
            print("\n=== ATENDIMENTOS MAIS BARATOS ===")
            for a in resultado["mais_baratos"]:
                print(f"  {a.data} | {a.paciente.nome} | R${a.calcular_valor_total():.2f}")
        except ValueError as e:
            print(f"Erro: {e}")

    def procedimentos_mais_populares(self):
        try:
            ranking = self.__controlador_procedimento.relatorio_mais_populares()
            print("\n=== PROCEDIMENTOS MAIS REALIZADOS ===")
            for i, (descricao, qtd) in enumerate(ranking):
                print(f"{i+1}. {descricao} | Realizações: {qtd}")
        except ValueError as e:
            print(f"Erro: {e}")

    def procedimentos_mais_caros_baratos(self):
        try:
            resultado = self.__controlador_procedimento.relatorio_mais_caros_baratos()
            print("\n=== PROCEDIMENTOS MAIS CAROS ===")
            for p in resultado["mais_caros"]:
                print(f"  {p.descricao} | R${p.calcular_custo():.2f}")
            print("\n=== PROCEDIMENTOS MAIS BARATOS ===")
            for p in resultado["mais_baratos"]:
                print(f"  {p.descricao} | R${p.calcular_custo():.2f}")
        except ValueError as e:
            print(f"Erro: {e}")
