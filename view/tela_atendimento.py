import FreeSimpleGUI as sg
from Exceptions.atendimentoException import AtendimentoException

class TelaAtendimento:
    def __init__(self, controlador_atendimento):
        self.__controlador_atendimento = controlador_atendimento

    def mostrar_menu(self):
        layout = [
            [sg.Text('=== MENU ATENDIMENTO ===', font=('Helvetica', 14, 'bold'))],
            [sg.Button('Registrar atendimento', key='1', size=(25, 1))],
            [sg.Button('Remover atendimento', key='2', size=(25, 1))],
            [sg.Button('Alterar atendimento', key='3', size=(25, 1))],
            [sg.Button('Listar atendimentos', key='4', size=(25, 1))],
            [sg.Button('Voltar', key='0', size=(10, 1), button_color=('white', 'gray'))]
        ]
        window = sg.Window('Menu Atendimento', layout, modal=True, element_justification='c')
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == '0':
                break
            elif event == '1':
                self.cadastrar()
            elif event == '2':
                self.remover()
            elif event == '3':
                self.alterar()
            elif event == '4':
                self.listar()
        window.close()

    def cadastrar(self):
        layout = [
            [sg.Text('Data do atendimento (AAAA-MM-DD):'), sg.InputText(key='data')],
            [sg.Text('Horário de início (HH:MM):'), sg.InputText(key='horario_inicio')],
            [sg.Text('Horário de fim (HH:MM):'), sg.InputText(key='horario_fim')],
            [sg.Text('Valor (R$):'), sg.InputText(key='valor')],
            [sg.Text('Nome da clínica:'), sg.InputText(key='nome_clinica')],
            [sg.Text('Cidade da clínica:'), sg.InputText(key='cidade_clinica')],
            [sg.Text('CPF do paciente:'), sg.InputText(key='cpf_paciente')],
            [sg.Text('CPF do profissional:'), sg.InputText(key='cpf_profissional')],
            [sg.Text('Tipo de atendimento:'), sg.InputText(key='nome_tipo')],
            [sg.Button('Registrar'), sg.Button('Cancelar', button_color=('white', 'gray'))]
        ]
        window = sg.Window('Registrar Atendimento', layout, modal=True)
        event, values = window.read()
        
        if event == 'Registrar':
            try:
                self.__controlador_atendimento.cadastrar(
                    values['data'].strip(), values['horario_inicio'].strip(), values['horario_fim'].strip(), float(values['valor'].strip()),
                    values['nome_clinica'].strip(), values['cidade_clinica'].strip(),
                    values['cpf_paciente'].strip(), values['cpf_profissional'].strip(), values['nome_tipo'].strip()
                )
                sg.popup('Atendimento registrado com sucesso!', title='Sucesso')
            except AtendimentoException as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
            except Exception as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
        window.close()

    def remover(self):
        layout = [
            [sg.Text('Número do atendimento a remover (índice 1-baseado):'), sg.InputText(key='index')],
            [sg.Button('Remover', button_color=('white', 'red')), sg.Button('Cancelar', button_color=('white', 'gray'))]
        ]
        window = sg.Window('Remover Atendimento', layout, modal=True)
        event, values = window.read()
        if event == 'Remover':
            try:
                index = int(values['index'].strip()) - 1
                self.__controlador_atendimento.remover(index)
                sg.popup('Atendimento removido com sucesso!', title='Sucesso')
            except AtendimentoException as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
            except ValueError:
                sg.popup_error('Erro: Número de atendimento inválido.', title='Erro')
        window.close()

    def alterar(self):
        layout = [
            [sg.Text('Número do atendimento a alterar:'), sg.InputText(key='index')],
            [sg.Text('Novos dados (deixe em branco para manter):', font=('Helvetica', 10, 'bold'))],
            [sg.Text('Nova data (AAAA-MM-DD):'), sg.InputText(key='data')],
            [sg.Text('Novo horário de início:'), sg.InputText(key='horario_inicio')],
            [sg.Text('Novo horário de fim:'), sg.InputText(key='horario_fim')],
            [sg.Text('Novo valor (R$):'), sg.InputText(key='valor')],
            [sg.Button('Alterar'), sg.Button('Cancelar', button_color=('white', 'gray'))]
        ]
        window = sg.Window('Alterar Atendimento', layout, modal=True)
        event, values = window.read()
        if event == 'Alterar':
            try:
                index = int(values['index'].strip()) - 1
                data = values['data'].strip() or None
                horario_inicio = values['horario_inicio'].strip() or None
                horario_fim = values['horario_fim'].strip() or None
                valor_str = values['valor'].strip()
                valor = float(valor_str) if valor_str else None
                
                self.__controlador_atendimento.alterar(index, data, horario_inicio, horario_fim, valor)
                sg.popup('Atendimento alterado com sucesso!', title='Sucesso')
            except AtendimentoException as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
            except Exception as e:
                sg.popup_error(f'Erro: {e}', title='Erro')
        window.close()

    def listar(self):
        try:
            atendimentos = self.__controlador_atendimento.listar()
            text = "=== ATENDIMENTOS ===\n\n"
            for i, a in enumerate(atendimentos):
                text += f"{i+1}. {a['data']} | {a['horario_inicio']}-{a['horario_fim']} | " \
                        f"{a['tipo_atendimento']} | Paciente: {a['paciente']} | " \
                        f"Profissional: {a['profissional']} | Clínica: {a['clinica']} | " \
                        f"Total: R${a['valor_total']:.2f} | Restante: R${a['valor_restante']:.2f}\n"
            sg.popup_scrolled(text, title='Listar Atendimentos', size=(80, 20))
        except AtendimentoException as e:
            sg.popup_error(f'Erro: {e}', title='Erro')
