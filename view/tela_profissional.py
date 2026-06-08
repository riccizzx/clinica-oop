from model.profissional import Profissional
from datetime import date

class TelaProfissional:
    def __init__(self, controlador_profissional):
        self.__controlador_profissional = controlador_profissional

    def mostrar_menu(self):
        while True:
            print("\n=== MENU PROFISSIONAL ===")
            print("1. Cadastrar profissional")
            print("2. Remover profissional")
            print("3. Alterar profissional")
            print("4. Listar profissionais")
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
            nome = input("Nome: ").strip()
            celular = input("Celular: ").strip()
            cpf = input("CPF (somente números): ").strip()
            data_str = input("Data de nascimento (DD/MM/AAAA): ").strip()
            data_nascimento = date(*reversed([int(x) for x in data_str.split("/")]))
            especialidade = input("Especialidade: ").strip()
            registro = input("Registro profissional: ").strip()
            profissional = Profissional(nome, celular, cpf, data_nascimento, especialidade, registro)
            self.__controlador_profissional.cadastrar(profissional)
            print("Profissional cadastrado com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def remover(self):
        try:
            cpf = input("CPF do profissional a remover: ").strip()
            self.__controlador_profissional.remover(cpf)
            print("Profissional removido com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def alterar(self):
        try:
            cpf = input("CPF do profissional a alterar: ").strip()
            print("Deixe em branco para manter o valor atual.")
            nome = input("Novo nome: ").strip() or None
            celular = input("Novo celular: ").strip() or None
            especialidade = input("Nova especialidade: ").strip() or None
            registro = input("Novo registro profissional: ").strip() or None
            self.__controlador_profissional.alterar(cpf, nome, celular, especialidade, registro)
            print("Profissional alterado com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def listar(self):
        try:
            profissionais = self.__controlador_profissional.listar()
            print("\n=== PROFISSIONAIS ===")
            for i, p in enumerate(profissionais):
                print(f"{i+1}. {p.nome} | CPF: {p.cpf} | Especialidade: {p.especialidade} | Registro: {p.registro_profissional}")
        except ValueError as e:
            print(f"Erro: {e}")