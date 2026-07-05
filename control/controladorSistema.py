import FreeSimpleGUI as sg
from control.controladorPaciente import ControladorPaciente
from control.controladorClinica import ControladorClinica
from control.controladorProfissional import ControladorProfissional
from control.controladorTipoAtendimento import ControladorTipoAtendimento
from control.controladorAtendimento import ControladorAtendimento
from control.controladorProcedimento import ControladorProcedimento
from control.controladorPagamento import ControladorPagamento

from view.tela_paciente import TelaPaciente
from view.tela_clinica import TelaClinica
from view.tela_profissional import TelaProfissional
from view.tela_tipo_atendimento import TelaTipoAtendimento
from view.tela_atendimento import TelaAtendimento
from view.tela_procedimento import TelaProcedimento
from view.tela_pagamento import TelaPagamento
from view.tela_relatorios import TelaRelatorios

class ControladorSistema:
    def __init__(self):
        # Controladores
        self.__controlador_paciente = ControladorPaciente()
        self.__controlador_clinica = ControladorClinica()
        self.__controlador_profissional = ControladorProfissional()
        self.__controlador_tipo_atendimento = ControladorTipoAtendimento()
        self.__controlador_atendimento = ControladorAtendimento(
            self.__controlador_paciente,
            self.__controlador_clinica,
            self.__controlador_profissional,
            self.__controlador_tipo_atendimento,
        )
        self.__controlador_procedimento = ControladorProcedimento(
            self.__controlador_profissional,
            self.__controlador_atendimento,
        )
        self.__controlador_pagamento = ControladorPagamento(
            self.__controlador_atendimento,
        )

        # Telas
        self.__tela_paciente = TelaPaciente(self.__controlador_paciente)
        self.__tela_clinica = TelaClinica(self.__controlador_clinica)
        self.__tela_profissional = TelaProfissional(self.__controlador_profissional)
        self.__tela_tipo_atendimento = TelaTipoAtendimento(self.__controlador_tipo_atendimento)
        self.__tela_atendimento = TelaAtendimento(self.__controlador_atendimento)
        self.__tela_procedimento = TelaProcedimento(self.__controlador_procedimento)
        self.__tela_pagamento = TelaPagamento(self.__controlador_pagamento)
        self.__tela_relatorios = TelaRelatorios(
            self.__controlador_atendimento,
            self.__controlador_procedimento,
        )

    def iniciar(self):
        sg.theme('LightBlue')
        layout = [
            [sg.Text('=== SISTEMA DE CLÍNICAS ===', font=('Helvetica', 16, 'bold'), justification='center', expand_x=True)],
            [sg.Frame('Cadastros', [
                [sg.Button('Pacientes', size=(15, 2)), sg.Button('Clínicas', size=(15, 2))],
                [sg.Button('Profissionais', size=(15, 2)), sg.Button('Tipos de atendimento', size=(15, 2))]
            ], expand_x=True, element_justification='c')],
            [sg.Frame('Registros', [
                [sg.Button('Atendimentos', size=(15, 2)), sg.Button('Procedimentos', size=(15, 2)), sg.Button('Pagamentos', size=(15, 2))]
            ], expand_x=True, element_justification='c')],
            [sg.Frame('Relatórios', [
                [sg.Button('Relatórios', size=(49, 2))]
            ], expand_x=True, element_justification='c')],
            [sg.Button('Sair', button_color=('white', 'red'), size=(10, 1))]
        ]
        
        window = sg.Window('Sistema de Clínicas', layout, element_justification='c')
        
        while True:
            event, values = window.read()
            
            if event == sg.WIN_CLOSED or event == 'Sair':
                break
            elif event == 'Pacientes':
                self.__tela_paciente.mostrar_menu()
            elif event == 'Clínicas':
                self.__tela_clinica.mostrar_menu()
            elif event == 'Profissionais':
                self.__tela_profissional.mostrar_menu()
            elif event == 'Tipos de atendimento':
                self.__tela_tipo_atendimento.mostrar_menu()
            elif event == 'Atendimentos':
                self.__tela_atendimento.mostrar_menu()
            elif event == 'Procedimentos':
                self.__tela_procedimento.mostrar_menu()
            elif event == 'Pagamentos':
                self.__tela_pagamento.mostrar_menu()
            elif event == 'Relatórios':
                self.__tela_relatorios.mostrar_menu()
                
        window.close()
