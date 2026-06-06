
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
from model.profissional import Profissional
from model.procedimento import Procedimento
from model.atendimento import Atendimento
from model.pagamento import Pagamento

# testando a classe paciente
def main():
    paciente_1 = Paciente( # exemplo cadastrando um paciente
        nome="Guilherme",
        celular="123456789",
        cpf="12345678900",
        data_nascimento=date(2006, 3, 15), # data invertida para evitar confusão entre dia e mês
    )
    print("Nome:    ", paciente_1.nome)
    print("Celular: ", paciente_1.celular)
    print("CPF:     ", paciente_1.cpf)
    print("Idade:   ", paciente_1.calcular_idade(paciente_1.data_nascimento))
    print("Menor?   ", paciente_1.verificar_idade() ,"\n")
    #print("CPF ok?  ", paciente.validar_cpf()).


    profissional_1= Profissional("Xande","47984897621", date(2000, 5, 16), "127.123.199-50", "Urologista", "CRM",)

    print("Nome:    ", profissional_1.nome)
    print("Celular: ", profissional_1.celular)
    print("CPF:     ", profissional_1.cpf)
    print("Idade:   ", profissional_1.calcular_idade(paciente_1.data_nascimento))

if __name__ == "__main__":
    main()
