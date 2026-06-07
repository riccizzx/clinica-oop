# Aqui será a implementação do controlador do sistema, onde serão implementados os métodos para realizar as operações do sistema, como cadastrar paciente, cadastrar atendimento, realizar pagamento, etc.

from control.controladorPaciente import ControladorPaciente
from control.controladorClinica import ControladorClinica
# from control.controladorProfissional import ControladorProfissional
# from control.controladorTipoAtendimento import ControladorTipoAtendimento
from control.controladorAtendimento import ControladorAtendimento
# from control.controladorProcedimento import ControladorProcedimento
# from control.controladorPagamento import ControladorPagamento

from view.tela_paciente import TelaPaciente
from view.tela_clinica import TelaClinica
# from view.tela_profissional import TelaProfissional
# from view.tela_tipo_atendimento import TelaTipoAtendimento
from view.tela_atendimento import TelaAtendimento
# from view.tela_procedimento import TelaProcedimento
# from view.tela_pagamento import TelaPagamento
from view.tela_relatorios import TelaRelatorios

class ControladorSistema:
    def __init__(self):
        # Controladores
        self.__controlador_paciente = ControladorPaciente()
        self.__controlador_clinica = ControladorClinica()
        # self.__controlador_profissional = ControladorProfissional()
        # self.__controlador_tipo_atendimento = ControladorTipoAtendimento()
        self.__controlador_atendimento = ControladorAtendimento(
            self.__controlador_paciente,
            self.__controlador_clinica,
            None,  # controlador_profissional - aguardando parte do Guilherme
            None,  # controlador_tipo_atendimento - aguardando parte do Guilherme
        )
        # self.__controlador_procedimento = ControladorProcedimento(
        #     self.__controlador_profissional,
        #     self.__controlador_atendimento,
        # )
        # self.__controlador_pagamento = ControladorPagamento(
        #     self.__controlador_atendimento,
        # )

        # Telas
        self.__tela_paciente = TelaPaciente(self.__controlador_paciente)
        self.__tela_clinica = TelaClinica(self.__controlador_clinica)
        # self.__tela_profissional = TelaProfissional(self.__controlador_profissional)
        # self.__tela_tipo_atendimento = TelaTipoAtendimento(self.__controlador_tipo_atendimento)
        self.__tela_atendimento = TelaAtendimento(self.__controlador_atendimento)
        # self.__tela_procedimento = TelaProcedimento(self.__controlador_procedimento)
        # self.__tela_pagamento = TelaPagamento(self.__controlador_pagamento)
        self.__tela_relatorios = TelaRelatorios(
            self.__controlador_atendimento,
            None,  # controlador_procedimento - aguardando parte do Guilherme
        )

    def iniciar(self):
        while True:
            print("\n=== SISTEMA DE CLÍNICAS ===")
            print("--- Cadastros ---")
            print("1. Pacientes")
            print("2. Clínicas")
            print("3. Profissionais")
            print("4. Tipos de atendimento")
            print("--- Registros ---")
            print("5. Atendimentos")
            print("6. Procedimentos")
            print("7. Pagamentos")
            print("--- Relatórios ---")
            print("8. Relatórios")
            print("0. Sair")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.__tela_paciente.mostrar_menu()
            elif opcao == "2":
                self.__tela_clinica.mostrar_menu()
            elif opcao == "3":
                self.__tela_profissional.mostrar_menu()
            elif opcao == "4":
                self.__tela_tipo_atendimento.mostrar_menu()
            elif opcao == "5":
                self.__tela_atendimento.mostrar_menu()
            elif opcao == "6":
                self.__tela_procedimento.mostrar_menu()
