
"""

main model para testes

o proposito desse arquivo é servir como testes para as classes do model, para verificar se estão funcionando
corretamente, e para servir como exemplo de como utilizar as classes do model.

sera deletada no futuro

"""
from .model.pessoa import Pessoa
from .model.paciente import Paciente
from .model.procedimento import Procedimento
from .model.atendimento import Atendimento
from .model.pagamento import Pagamento

def main():
    Paciente = Paciente("01/01/2000", "João", "123456789", "12345678900")
    print(Paciente.nome)
    print(Paciente.celular)
    print(Paciente.cpf)
    print(Paciente.calcular_idade(Paciente.data_nascimento))

if __name__ == "__main__":
    main()