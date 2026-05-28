
"""
DEIXAR CLARO QUE PODE OCORRER REFORMULAÇÕES NAS CLASSES, POIS AINDA ESTAMOS NA FASE DE PLANEJAMENTO

Com base na arquitetura (MVC) Model-View-Controller, o módulo Clinica é responsável por representar a lógica de negócio do sistema,
ou seja, as classes e funções que definem o comportamento do sistema e como ele deve funcionar.

Clinica é o módulo principal do projeto, onde estão as classes e funções que representam a lógica de negócio do sistema.

Com base no diagrama do model, basta escrever as classes nesta pasta model

"""

class Clinica:
    def __init__(self, nome, endereco, horario_abertura, horario_fechamento):
        self.__nome = nome
        self.__endereco = endereco
        self.__horario_abertura = horario_abertura
        self.__horario_fechamento = horario_fechamento

    @property
    def nome(self):
        return self.__nome
    
    @property
    def endereco(self):
        return self.__endereco
    
    @property
    def horario_abertura(self):
        return self.__horario_abertura

    @property
    def horario_fechamento(self):
        return self.__horario_fechamento

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @horario_abertura.setter
    def horario_abertura(self, horario_abertura):
        self.__horario_abertura = horario_abertura

    @horario_fechamento.setter
    def horario_fechamento(self, horario_fechamento):
        self.__horario_fechamento = horario_fechamento

    # métodos;
    def esta_aberta(self, horario_atual) -> bool:
        if self.__horario_abertura <= horario_atual < self.__horario_fechamento:
            return True
        else:
            return False
        
    def validar_horario_atendimento(self, horario_inicio, horario_fim) -> bool:
        if self.esta_aberta(horario_inicio) and self.esta_aberta(horario_fim) and horario_inicio < horario_fim:
            return True
        else:
            return False