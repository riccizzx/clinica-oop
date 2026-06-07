from model.clinica import Clinica

class TelaClinica:
    def __init__(self, controlador_clinica):
        self.__controlador_clinica = controlador_clinica

    def mostrar_menu(self):
        while True:
            print("\n=== MENU CLÍNICA ===")
            print("1. Cadastrar clínica")
            print("2. Remover clínica")
            print("3. Alterar clínica")
            print("4. Listar clínicas")
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
            nome = input("Nome da clínica: ").strip()
            cidade = input("Cidade: ").strip()
            horario_abertura = input("Horário de abertura (HH:MM): ").strip()
            horario_fechamento = input("Horário de fechamento (HH:MM): ").strip()
            clinica = Clinica(nome, cidade, horario_abertura, horario_fechamento)
            self.__controlador_clinica.cadastrar(clinica)
            print("Clínica cadastrada com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def remover(self):
        try:
            nome = input("Nome da clínica a remover: ").strip()
            cidade = input("Cidade: ").strip()
            self.__controlador_clinica.remover(nome, cidade)
            print("Clínica removida com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def alterar(self):
        try:
            nome = input("Nome da clínica a alterar: ").strip()
            cidade = input("Cidade: ").strip()
            print("Deixe em branco para manter o valor atual.")
            novo_nome = input("Novo nome: ").strip() or None
            nova_cidade = input("Nova cidade: ").strip() or None
            horario_abertura = input("Novo horário de abertura (HH:MM): ").strip() or None
            horario_fechamento = input("Novo horário de fechamento (HH:MM): ").strip() or None
            self.__controlador_clinica.alterar(nome, cidade, novo_nome, nova_cidade, horario_abertura, horario_fechamento)
            print("Clínica alterada com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def listar(self):
        try:
            clinicas = self.__controlador_clinica.listar()
            print("\n=== CLÍNICAS ===")
            for i, c in enumerate(clinicas):
                print(f"{i+1}. {c.nome} | Cidade: {c.cidade} | Funciona: {c.horario_abertura} às {c.horario_fechamento}")
        except ValueError as e:
            print(f"Erro: {e}")
