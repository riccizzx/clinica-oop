class TelaAtendimento:
    def __init__(self, controlador_atendimento):
        self.__controlador_atendimento = controlador_atendimento

    def mostrar_menu(self):
        while True:
            print("\n=== MENU ATENDIMENTO ===")
            print("1. Registrar atendimento")
            print("2. Remover atendimento")
            print("3. Alterar atendimento")
            print("4. Listar atendimentos")
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
            data = input("Data do atendimento (AAAA-MM-DD): ").strip()
            horario_inicio = input("Horário de início (HH:MM): ").strip()
            horario_fim = input("Horário de fim (HH:MM): ").strip()
            valor = float(input("Valor (R$): ").strip())
            nome_clinica = input("Nome da clínica: ").strip()
            cidade_clinica = input("Cidade da clínica: ").strip()
            cpf_paciente = input("CPF do paciente: ").strip()
            cpf_profissional = input("CPF do profissional: ").strip()
            nome_tipo = input("Tipo de atendimento: ").strip()

            self.__controlador_atendimento.cadastrar(
                data, horario_inicio, horario_fim, valor,
                nome_clinica, cidade_clinica,
                cpf_paciente, cpf_profissional, nome_tipo
            )
            print("Atendimento registrado com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def remover(self):
        try:
            self.listar()
            index = int(input("Número do atendimento a remover: ").strip()) - 1
            self.__controlador_atendimento.remover(index)
            print("Atendimento removido com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def alterar(self):
        try:
            self.listar()
            index = int(input("Número do atendimento a alterar: ").strip()) - 1
            print("Deixe em branco para manter o valor atual.")
            data = input("Nova data (AAAA-MM-DD): ").strip() or None
            horario_inicio = input("Novo horário de início (HH:MM): ").strip() or None
            horario_fim = input("Novo horário de fim (HH:MM): ").strip() or None
            valor_str = input("Novo valor (R$): ").strip()
            valor = float(valor_str) if valor_str else None
            self.__controlador_atendimento.alterar(index, data, horario_inicio, horario_fim, valor)
            print("Atendimento alterado com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def listar(self):
        try:
            atendimentos = self.__controlador_atendimento.listar()
            print("\n=== ATENDIMENTOS ===")
            for i, a in enumerate(atendimentos):
                print(
                    f"{i+1}. {a.data} | {a.horario_inicio}-{a.horario_fim} | "
                    f"{a.tipo_atendimento.nome} | Paciente: {a.paciente.nome} | "
                    f"Profissional: {a.profissional.nome} | Clínica: {a.clinica.nome} | "
                    f"Total: R${a.calcular_valor_total():.2f} | Restante: R${a.calcular_valor_restante():.2f}"
                )
        except ValueError as e:
            print(f"Erro: {e}")
