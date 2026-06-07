from model.paciente import Paciente
from datetime import date

class TelaPaciente:
    def __init__(self, controlador_paciente):
        self.__controlador_paciente = controlador_paciente

    def mostrar_menu(self):
        while True:
            print("\n=== MENU PACIENTE ===")
            print("1. Cadastrar paciente")
            print("2. Remover paciente")
            print("3. Alterar paciente")
            print("4. Listar pacientes")
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

            paciente = Paciente(nome, celular, cpf, data_nascimento)

            if paciente.verificar_idade():
                print("Paciente menor de idade. Informe o responsável.")
                nome_resp = input("Nome do responsável: ").strip()
                cpf_resp = input("CPF do responsável (somente números): ").strip()
                paciente.nome_responsavel = nome_resp
                paciente.cpf_responsavel = cpf_resp

            self.__controlador_paciente.cadastrar(paciente)
            print("Paciente cadastrado com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def remover(self):
        try:
            cpf = input("CPF do paciente a remover: ").strip()
            self.__controlador_paciente.remover(cpf)
            print("Paciente removido com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def alterar(self):
        try:
            cpf = input("CPF do paciente a alterar: ").strip()
            print("Deixe em branco para manter o valor atual.")
            nome = input("Novo nome: ").strip() or None
            celular = input("Novo celular: ").strip() or None
            nome_resp = input("Novo nome do responsável: ").strip() or None
            cpf_resp = input("Novo CPF do responsável: ").strip() or None
            self.__controlador_paciente.alterar(cpf, nome, celular, nome_resp, cpf_resp)
            print("Paciente alterado com sucesso!")
        except ValueError as e:
            print(f"Erro: {e}")

    def listar(self):
        try:
            pacientes = self.__controlador_paciente.listar()
            print("\n=== PACIENTES ===")
            for i, p in enumerate(pacientes):
                print(f"{i+1}. {p.nome} | CPF: {p.cpf} | Celular: {p.celular} | Nascimento: {p.data_nascimento}")
        except ValueError as e:
            print(f"Erro: {e}")
