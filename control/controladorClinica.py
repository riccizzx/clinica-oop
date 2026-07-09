from model.clinica import Clinica
from Exceptions.clinicaException import ClinicaException

class ControladorClinica:
    def __init__(self, controlador_profissional):
        self.__clinicas = []
        self.__controlador_profissional = controlador_profissional

    def cadastrar(self, nome, cidade, horario_abertura, horario_fechamento):
        for c in self.__clinicas:
            if c.nome == nome and c.cidade == cidade:
                raise ClinicaException(f"Já existe uma clínica com o nome '{nome}' em {cidade}.")
        clinica = Clinica(nome, cidade, horario_abertura, horario_fechamento)
        self.__clinicas.append(clinica)

    def remover(self, nome, cidade):
        clinica = self.buscar(nome, cidade)
        self.__clinicas.remove(clinica)

    def alterar(self, nome, cidade, novo_nome=None, nova_cidade=None, horario_abertura=None, horario_fechamento=None):
        clinica = self.buscar(nome, cidade)
        if novo_nome:
            clinica.nome = novo_nome
        if nova_cidade:
            clinica.cidade = nova_cidade
        if horario_abertura:
            clinica.horario_abertura = horario_abertura
        if horario_fechamento:
            clinica.horario_fechamento = horario_fechamento

    def listar(self):
        if not self.__clinicas:
            raise ClinicaException("Nenhuma clínica cadastrada.")
        
        return [
            {
                "nome": c.nome,
                "cidade": c.cidade,
                "horario_abertura": c.horario_abertura,
                "horario_fechamento": c.horario_fechamento,
                "profissionais": [p.nome for p in c.profissionais]
            }
            for c in self.__clinicas
        ]

    def buscar(self, nome, cidade):
        for c in self.__clinicas:
            if c.nome == nome and c.cidade == cidade:
                return c
        raise ClinicaException(f"Clínica '{nome}' em {cidade} não encontrada.")

    def vincular_profissional(self, nome, cidade, cpf_profissional):
        # Exemplo de agregação em uso: associa um Profissional já cadastrado a uma Clinica.
        clinica = self.buscar(nome, cidade)
        profissional = self.__controlador_profissional.buscar_por_cpf(cpf_profissional)
        clinica.adicionar_profissional(profissional)

    def desvincular_profissional(self, nome, cidade, cpf_profissional):
        clinica = self.buscar(nome, cidade)
        profissional = self.__controlador_profissional.buscar_por_cpf(cpf_profissional)
        clinica.remover_profissional(profissional)
