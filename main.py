
"""

main.py — arquivo de testes para as classes do model.

Serve para verificar se as classes estão funcionando corretamente
e como exemplo de uso. Será removido futuramente.

para executar siga - 
    cd clinica
    command - python -m main || python main.py

"""

from datetime import date

from model.pessoa import Pessoa
from model.paciente import Paciente
from model.procedimento import Procedimento
from model.atendimento import Atendimento
from model.pagamento import Pagamento

# testando a classe paciente
def main():
    paciente = Paciente(
        nome="Guilherme",
        celular="123456789",
        cpf="12345678900",
        data_nascimento=date(2006, 3, 15), # data invertida para evitar confusão entre dia e mês
        #data_nascimento = date(15, 3, 2006)
    )

    print("Nome:    ", paciente.nome)
    print("Celular: ", paciente.celular)
    print("CPF:     ", paciente.cpf)
    print("Idade:   ", paciente.calcular_idade(paciente.data_nascimento))
    print("Menor?   ", paciente.verificar_idade())
    #print("CPF ok?  ", paciente.validar_cpf())


if __name__ == "__main__":
    main()
