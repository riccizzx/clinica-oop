"""
testes.py — testes automatizados do sistema de clínicas.
Cobre todos os cadastros, registros, relatórios, regras de negócio e exceções.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from datetime import date
from model.paciente import Paciente
from model.profissional import Profissional
from model.clinica import Clinica
from model.tipo_atendimento import TipoAtendimento
from model.procedimento import Procedimento
from model.pagamentoDinheiro import PagamentoDinheiro
from model.pagamentoPix import PagamentoPix
from model.pagamentoCartao import PagamentoCartao
from control.controladorPaciente import ControladorPaciente
from control.controladorClinica import ControladorClinica
from control.controladorProfissional import ControladorProfissional
from control.controladorTipoAtendimento import ControladorTipoAtendimento
from control.controladorAtendimento import ControladorAtendimento
from control.controladorProcedimento import ControladorProcedimento
from control.controladorPagamento import ControladorPagamento

PASSOU = 0
FALHOU = 0

def teste(nome, fn):
    global PASSOU, FALHOU
    try:
        fn()
        print(f"  [OK] {nome}")
        PASSOU += 1
    except Exception as e:
        print(f"  [FALHOU] {nome}")
        print(f"           {type(e).__name__}: {e}")
        FALHOU += 1

def espera_excecao(nome, excecao, fn):
    global PASSOU, FALHOU
    try:
        fn()
        print(f"  [FALHOU] {nome} — esperava {excecao.__name__}, nenhuma exceção foi lançada")
        FALHOU += 1
    except excecao:
        print(f"  [OK] {nome}")
        PASSOU += 1
    except Exception as e:
        print(f"  [FALHOU] {nome} — esperava {excecao.__name__}, recebeu {type(e).__name__}: {e}")
        FALHOU += 1

# ── fixtures ──────────────────────────────────────────────────────────────────

def make_sistema():
    cp = ControladorPaciente()
    cc = ControladorClinica()
    cpr = ControladorProfissional()
    ct = ControladorTipoAtendimento()
    ca = ControladorAtendimento(cp, cc, cpr, ct)
    cpro = ControladorProcedimento(cpr, ca)
    cpag = ControladorPagamento(ca)
    return cp, cc, cpr, ct, ca, cpro, cpag

def paciente_adulto():
    return Paciente("Ana Silva", "48999990000", "12345678901", date(1990, 5, 10))

def paciente_menor():
    return Paciente("João Menor", "48988880000", "98765432100", date(2010, 3, 20),
                    nome_responsavel="Maria Menor", cpf_responsavel="11122233344")

def paciente_menor_sem_resp():
    return Paciente("Pedro Menor", "48977770000", "55566677788", date(2012, 1, 1))

def profissional_valido():
    return Profissional("Dr. Carlos", "48966660000", "44455566677", date(1975, 8, 15), "Cardiologia", "CRM12345")

def clinica_valida():
    return Clinica("Clínica Vida", "Florianópolis", "08:00", "18:00")

def tipo_valido():
    return TipoAtendimento("Consulta", "Consulta geral", 150.0)

def setup_completo():
    cp, cc, cpr, ct, ca, cpro, cpag = make_sistema()
    cp.cadastrar(paciente_adulto())
    cc.cadastrar(clinica_valida())
    cpr.cadastrar(profissional_valido())
    ct.cadastrar(tipo_valido())
    return cp, cc, cpr, ct, ca, cpro, cpag


# ══════════════════════════════════════════════════════════════════════════════
# 1. CADASTRO DE PACIENTE
# ══════════════════════════════════════════════════════════════════════════════
print("\n═══ 1. CADASTRO DE PACIENTE ═══")

def t_cadastrar_paciente():
    cp, *_ = make_sistema()
    cp.cadastrar(paciente_adulto())
    assert len(cp.listar()) == 1
teste("Cadastrar paciente adulto", t_cadastrar_paciente)

def t_cadastrar_paciente_menor_com_resp():
    cp, *_ = make_sistema()
    cp.cadastrar(paciente_menor())
    assert len(cp.listar()) == 1
teste("Cadastrar paciente menor com responsável", t_cadastrar_paciente_menor_com_resp)

espera_excecao("Cadastrar paciente menor sem responsável lança ValueError", ValueError,
    lambda: ControladorPaciente().cadastrar(paciente_menor_sem_resp()))

def t_cpf_duplicado_paciente():
    cp, *_ = make_sistema()
    cp.cadastrar(paciente_adulto())
    cp.cadastrar(paciente_adulto())
espera_excecao("CPF duplicado em paciente lança ValueError", ValueError,
    t_cpf_duplicado_paciente)

def t_cpf_invalido_paciente():
    cp, *_ = make_sistema()
    p = Paciente("Teste", "48900000000", "123", date(1990, 1, 1))
    cp.cadastrar(p)
espera_excecao("CPF inválido em paciente lança ValueError", ValueError,
    t_cpf_invalido_paciente)

def t_alterar_paciente():
    cp, *_ = make_sistema()
    cp.cadastrar(paciente_adulto())
    cp.alterar("12345678901", nome="Ana Souza")
    assert cp.buscar_por_cpf("12345678901").nome == "Ana Souza"
teste("Alterar paciente", t_alterar_paciente)

def t_remover_paciente():
    cp, *_ = make_sistema()
    cp.cadastrar(paciente_adulto())
    cp.remover("12345678901")
    espera_excecao("Listar após remover único paciente lança ValueError", ValueError, cp.listar)
teste("Remover paciente", t_remover_paciente)

espera_excecao("Buscar paciente inexistente lança ValueError", ValueError,
    lambda: ControladorPaciente().buscar_por_cpf("00000000000"))

espera_excecao("Listar pacientes com lista vazia lança ValueError", ValueError,
    lambda: ControladorPaciente().listar())


# ══════════════════════════════════════════════════════════════════════════════
# 2. CADASTRO DE CLÍNICA
# ══════════════════════════════════════════════════════════════════════════════
print("\n═══ 2. CADASTRO DE CLÍNICA ═══")

def t_cadastrar_clinica():
    cc = ControladorClinica()
    cc.cadastrar(clinica_valida())
    assert len(cc.listar()) == 1
teste("Cadastrar clínica", t_cadastrar_clinica)

def t_clinica_duplicada():
    cc = ControladorClinica()
    cc.cadastrar(clinica_valida())
    cc.cadastrar(clinica_valida())
espera_excecao("Clínica duplicada lança ValueError", ValueError, t_clinica_duplicada)

def t_alterar_clinica():
    cc = ControladorClinica()
    cc.cadastrar(clinica_valida())
    cc.alterar("Clínica Vida", "Florianópolis", novo_nome="Clínica Nova")
    assert cc.buscar("Clínica Nova", "Florianópolis").nome == "Clínica Nova"
teste("Alterar clínica", t_alterar_clinica)

def t_remover_clinica():
    cc = ControladorClinica()
    cc.cadastrar(clinica_valida())
    cc.remover("Clínica Vida", "Florianópolis")
    espera_excecao("Listar após remover única clínica lança ValueError", ValueError, cc.listar)
teste("Remover clínica", t_remover_clinica)

espera_excecao("Buscar clínica inexistente lança ValueError", ValueError,
    lambda: ControladorClinica().buscar("Inexistente", "Cidade"))


# ══════════════════════════════════════════════════════════════════════════════
# 3. CADASTRO DE PROFISSIONAL
# ══════════════════════════════════════════════════════════════════════════════
print("\n═══ 3. CADASTRO DE PROFISSIONAL ═══")

def t_cadastrar_profissional():
    cpr = ControladorProfissional()
    cpr.cadastrar(profissional_valido())
    assert len(cpr.listar()) == 1
teste("Cadastrar profissional", t_cadastrar_profissional)

def t_cpf_duplicado_profissional():
    cpr = ControladorProfissional()
    cpr.cadastrar(profissional_valido())
    cpr.cadastrar(profissional_valido())
espera_excecao("CPF duplicado em profissional lança ValueError", ValueError,
    t_cpf_duplicado_profissional)

def t_registro_invalido():
    cpr = ControladorProfissional()
    p = Profissional("Dr. Sem Registro", "48900000000", "99988877766", date(1980, 1, 1), "Clínica", "")
    cpr.cadastrar(p)
espera_excecao("Registro profissional vazio lança ValueError", ValueError,
    t_registro_invalido)

def t_alterar_profissional():
    cpr = ControladorProfissional()
    cpr.cadastrar(profissional_valido())
    cpr.alterar("44455566677", especialidade="Neurologia")
    assert cpr.buscar_por_cpf("44455566677").especialidade == "Neurologia"
teste("Alterar profissional", t_alterar_profissional)

def t_remover_profissional():
    cpr = ControladorProfissional()
    cpr.cadastrar(profissional_valido())
    cpr.remover("44455566677")
    espera_excecao("Listar após remover único profissional lança ValueError", ValueError, cpr.listar)
teste("Remover profissional", t_remover_profissional)


# ══════════════════════════════════════════════════════════════════════════════
# 4. CADASTRO DE TIPO DE ATENDIMENTO
# ══════════════════════════════════════════════════════════════════════════════
print("\n═══ 4. CADASTRO DE TIPO DE ATENDIMENTO ═══")

def t_cadastrar_tipo():
    ct = ControladorTipoAtendimento()
    ct.cadastrar(tipo_valido())
    assert len(ct.listar()) == 1
teste("Cadastrar tipo de atendimento", t_cadastrar_tipo)

def t_tipo_duplicado():
    ct = ControladorTipoAtendimento()
    ct.cadastrar(tipo_valido())
    ct.cadastrar(tipo_valido())
espera_excecao("Tipo duplicado lança ValueError", ValueError, t_tipo_duplicado)

def t_alterar_tipo():
    ct = ControladorTipoAtendimento()
    ct.cadastrar(tipo_valido())
    ct.alterar("Consulta", novo_nome="Retorno", valor_base=80.0)
    assert ct.buscar("Retorno").valor_base == 80.0
teste("Alterar tipo de atendimento", t_alterar_tipo)

def t_remover_tipo():
    ct = ControladorTipoAtendimento()
    ct.cadastrar(tipo_valido())
    ct.remover("Consulta")
    espera_excecao("Listar após remover único tipo lança ValueError", ValueError, ct.listar)
teste("Remover tipo de atendimento", t_remover_tipo)


# ══════════════════════════════════════════════════════════════════════════════
# 5. REGISTRO DE ATENDIMENTO
# ══════════════════════════════════════════════════════════════════════════════
print("\n═══ 5. REGISTRO DE ATENDIMENTO ═══")

def t_cadastrar_atendimento():
    cp, cc, cpr, ct, ca, *_ = setup_completo()
    ca.cadastrar("2026-06-10", "09:00", "10:00", 150.0,
                 "Clínica Vida", "Florianópolis", "12345678901", "44455566677", "Consulta")
    assert len(ca.listar()) == 1
teste("Cadastrar atendimento", t_cadastrar_atendimento)

def t_atendimento_fora_horario():
    cp, cc, cpr, ct, ca, *_ = setup_completo()
    ca.cadastrar("2026-06-10", "07:00", "08:00", 150.0,
                 "Clínica Vida", "Florianópolis", "12345678901", "44455566677", "Consulta")
espera_excecao("Atendimento fora do horário da clínica lança ValueError", ValueError,
    t_atendimento_fora_horario)

def t_atendimento_paciente_menor_sem_resp():
    cp, cc, cpr, ct, ca, *_ = make_sistema()
    p = Paciente("Menor Sem Resp", "48900000000", "55566677788", date(2012, 1, 1))
    cp.cadastrar(p)
    cc.cadastrar(clinica_valida())
    cpr.cadastrar(profissional_valido())
    ct.cadastrar(tipo_valido())
    ca.cadastrar("2026-06-10", "09:00", "10:00", 150.0,
                 "Clínica Vida", "Florianópolis", "55566677788", "44455566677", "Consulta")
espera_excecao("Atendimento de menor sem responsável lança ValueError", ValueError,
    t_atendimento_paciente_menor_sem_resp)

def t_alterar_atendimento():
    cp, cc, cpr, ct, ca, *_ = setup_completo()
    ca.cadastrar("2026-06-10", "09:00", "10:00", 150.0,
                 "Clínica Vida", "Florianópolis", "12345678901", "44455566677", "Consulta")
    ca.alterar(0, valor=200.0)
    assert ca.buscar(0).valor == 200.0
teste("Alterar atendimento", t_alterar_atendimento)

def t_remover_atendimento():
    cp, cc, cpr, ct, ca, *_ = setup_completo()
    ca.cadastrar("2026-06-10", "09:00", "10:00", 150.0,
                 "Clínica Vida", "Florianópolis", "12345678901", "44455566677", "Consulta")
    ca.remover(0)
    espera_excecao("Listar após remover único atendimento lança ValueError", ValueError, ca.listar)
teste("Remover atendimento", t_remover_atendimento)

espera_excecao("Buscar atendimento com index inválido lança ValueError", ValueError,
    lambda: ControladorAtendimento(None, None, None, None).buscar(99))


# ══════════════════════════════════════════════════════════════════════════════
# 6. REGISTRO DE PROCEDIMENTO
# ══════════════════════════════════════════════════════════════════════════════
print("\n═══ 6. REGISTRO DE PROCEDIMENTO ═══")

def t_cadastrar_procedimento():
    cp, cc, cpr, ct, ca, cpro, cpag = setup_completo()
    ca.cadastrar("2026-06-10", "09:00", "10:00", 150.0,
                 "Clínica Vida", "Florianópolis", "12345678901", "44455566677", "Consulta")
    cpro.cadastrar("Eletrocardiograma", 80.0, "44455566677", 0)
    assert len(cpro.listar()) == 1
    assert ca.buscar(0).calcular_valor_total() == 230.0
teste("Cadastrar procedimento e atualizar valor total do atendimento", t_cadastrar_procedimento)

def t_alterar_procedimento():
    cp, cc, cpr, ct, ca, cpro, cpag = setup_completo()
    ca.cadastrar("2026-06-10", "09:00", "10:00", 150.0,
                 "Clínica Vida", "Florianópolis", "12345678901", "44455566677", "Consulta")
    cpro.cadastrar("Eletrocardiograma", 80.0, "44455566677", 0)
    cpro.alterar(0, descricao="ECG Completo", custo=100.0)
    assert cpro.buscar(0).descricao == "ECG Completo"
    assert cpro.buscar(0).custo == 100.0
teste("Alterar procedimento", t_alterar_procedimento)

def t_remover_procedimento():
    cp, cc, cpr, ct, ca, cpro, cpag = setup_completo()
    ca.cadastrar("2026-06-10", "09:00", "10:00", 150.0,
                 "Clínica Vida", "Florianópolis", "12345678901", "44455566677", "Consulta")
    cpro.cadastrar("Eletrocardiograma", 80.0, "44455566677", 0)
    cpro.remover(0)
    espera_excecao("Listar após remover único procedimento lança ValueError", ValueError, cpro.listar)
teste("Remover procedimento", t_remover_procedimento)

def t_procedimento_profissional_inexistente():
    cp, cc, cpr, ct, ca, cpro, cpag = setup_completo()
    ca.cadastrar("2026-06-10", "09:00", "10:00", 150.0,
                 "Clínica Vida", "Florianópolis", "12345678901", "44455566677", "Consulta")
    cpro.cadastrar("ECG", 80.0, "00000000000", 0)
espera_excecao("Procedimento com profissional inexistente lança ValueError", ValueError,
    t_procedimento_profissional_inexistente)


# ══════════════════════════════════════════════════════════════════════════════
# 7. REGISTRO DE PAGAMENTO
# ══════════════════════════════════════════════════════════════════════════════
print("\n═══ 7. REGISTRO DE PAGAMENTO ═══")

def t_pagamento_dinheiro():
    cp, cc, cpr, ct, ca, cpro, cpag = setup_completo()
    ca.cadastrar("2026-06-10", "09:00", "10:00", 150.0,
                 "Clínica Vida", "Florianópolis", "12345678901", "44455566677", "Consulta")
    cpag.cadastrar("dinheiro", "2026-06-10", 150.0, 0)
    assert not ca.buscar(0).verificar_pagamento_pendente()
teste("Pagamento em dinheiro", t_pagamento_dinheiro)

def t_pagamento_pix():
    cp, cc, cpr, ct, ca, cpro, cpag = setup_completo()
    ca.cadastrar("2026-06-10", "09:00", "10:00", 150.0,
                 "Clínica Vida", "Florianópolis", "12345678901", "44455566677", "Consulta")
    cpag.cadastrar("pix", "2026-06-10", 150.0, 0, cpf_pagador="12345678901")
    assert not ca.buscar(0).verificar_pagamento_pendente()
teste("Pagamento via PIX", t_pagamento_pix)

def t_pagamento_cartao():
    cp, cc, cpr, ct, ca, cpro, cpag = setup_completo()
    ca.cadastrar("2026-06-10", "09:00", "10:00", 150.0,
                 "Clínica Vida", "Florianópolis", "12345678901", "44455566677", "Consulta")
    cpag.cadastrar("cartao", "2026-06-10", 150.0, 0,
                   numero_cartao="1234567890123456", bandeira_cartao="Visa")
    assert not ca.buscar(0).verificar_pagamento_pendente()
teste("Pagamento via cartão", t_pagamento_cartao)

def t_pagamento_parcial():
    cp, cc, cpr, ct, ca, cpro, cpag = setup_completo()
    ca.cadastrar("2026-06-10", "09:00", "10:00", 150.0,
                 "Clínica Vida", "Florianópolis", "12345678901", "44455566677", "Consulta")
    cpag.cadastrar("dinheiro", "2026-06-10", 80.0, 0)
    assert ca.buscar(0).verificar_pagamento_pendente()
    assert ca.buscar(0).calcular_valor_restante() == 70.0
    cpag.cadastrar("dinheiro", "2026-06-10", 70.0, 0)
    assert not ca.buscar(0).verificar_pagamento_pendente()
teste("Pagamento parcial (parcelamento)", t_pagamento_parcial)

def t_pagamento_apos_data():
    cp, cc, cpr, ct, ca, cpro, cpag = setup_completo()
    ca.cadastrar("2026-06-10", "09:00", "10:00", 150.0,
                 "Clínica Vida", "Florianópolis", "12345678901", "44455566677", "Consulta")
    cpag.cadastrar("dinheiro", "2026-06-15", 150.0, 0)
espera_excecao("Pagamento após data do atendimento lança ValueError", ValueError,
    t_pagamento_apos_data)

def t_pagamento_pix_sem_cpf():
    cp, cc, cpr, ct, ca, cpro, cpag = setup_completo()
    ca.cadastrar("2026-06-10", "09:00", "10:00", 150.0,
                 "Clínica Vida", "Florianópolis", "12345678901", "44455566677", "Consulta")
    cpag.cadastrar("pix", "2026-06-10", 150.0, 0)
espera_excecao("PIX sem CPF do pagador lança ValueError", ValueError,
    t_pagamento_pix_sem_cpf)

def t_pagamento_cartao_sem_dados():
    cp, cc, cpr, ct, ca, cpro, cpag = setup_completo()
    ca.cadastrar("2026-06-10", "09:00", "10:00", 150.0,
                 "Clínica Vida", "Florianópolis", "12345678901", "44455566677", "Consulta")
    cpag.cadastrar("cartao", "2026-06-10", 150.0, 0)
espera_excecao("Cartão sem número e bandeira lança ValueError", ValueError,
    t_pagamento_cartao_sem_dados)

def t_pagamento_tipo_invalido():
    cp, cc, cpr, ct, ca, cpro, cpag = setup_completo()
    ca.cadastrar("2026-06-10", "09:00", "10:00", 150.0,
                 "Clínica Vida", "Florianópolis", "12345678901", "44455566677", "Consulta")
    cpag.cadastrar("boleto", "2026-06-10", 150.0, 0)
espera_excecao("Tipo de pagamento inválido lança ValueError", ValueError,
    t_pagamento_tipo_invalido)

def t_atendimento_ja_pago():
    cp, cc, cpr, ct, ca, cpro, cpag = setup_completo()
    ca.cadastrar("2026-06-10", "09:00", "10:00", 150.0,
                 "Clínica Vida", "Florianópolis", "12345678901", "44455566677", "Consulta")
    cpag.cadastrar("dinheiro", "2026-06-10", 150.0, 0)
    cpag.cadastrar("dinheiro", "2026-06-10", 50.0, 0)
espera_excecao("Pagar atendimento já quitado lança ValueError", ValueError,
    t_atendimento_ja_pago)

def t_alterar_pagamento():
    cp, cc, cpr, ct, ca, cpro, cpag = setup_completo()
    ca.cadastrar("2026-06-10", "09:00", "10:00", 150.0,
                 "Clínica Vida", "Florianópolis", "12345678901", "44455566677", "Consulta")
    cpag.cadastrar("dinheiro", "2026-06-10", 150.0, 0)
    cpag.alterar(0, valor_pago=200.0)
    assert cpag.buscar(0).valor_pago == 200.0
teste("Alterar pagamento", t_alterar_pagamento)

def t_remover_pagamento():
    cp, cc, cpr, ct, ca, cpro, cpag = setup_completo()
    ca.cadastrar("2026-06-10", "09:00", "10:00", 150.0,
                 "Clínica Vida", "Florianópolis", "12345678901", "44455566677", "Consulta")
    cpag.cadastrar("dinheiro", "2026-06-10", 150.0, 0)
    cpag.remover(0)
    espera_excecao("Listar após remover único pagamento lança ValueError", ValueError, cpag.listar)
teste("Remover pagamento", t_remover_pagamento)


# ══════════════════════════════════════════════════════════════════════════════
# 8. RELATÓRIOS
# ══════════════════════════════════════════════════════════════════════════════
print("\n═══ 8. RELATÓRIOS ═══")

def setup_relatorios():
    cp, cc, cpr, ct, ca, cpro, cpag = setup_completo()
    clinica2 = Clinica("Clínica Saúde", "Joinville", "07:00", "19:00")
    cc.cadastrar(clinica2)
    ca.cadastrar("2026-06-10", "09:00", "10:00", 500.0,
                 "Clínica Vida", "Florianópolis", "12345678901", "44455566677", "Consulta")
    ca.cadastrar("2026-06-11", "10:00", "11:00", 100.0,
                 "Clínica Saúde", "Joinville", "12345678901", "44455566677", "Consulta")
    ca.cadastrar("2026-06-12", "09:00", "10:00", 300.0,
                 "Clínica Vida", "Florianópolis", "12345678901", "44455566677", "Consulta")
    cpro.cadastrar("Eletrocardiograma", 80.0, "44455566677", 0)
    cpro.cadastrar("Eletrocardiograma", 80.0, "44455566677", 1)
    cpro.cadastrar("Raio-X", 50.0, "44455566677", 2)
    return cp, cc, cpr, ct, ca, cpro, cpag

def t_relatorio_clinicas():
    cp, cc, cpr, ct, ca, cpro, cpag = setup_relatorios()
    ranking = ca.relatorio_clinicas_mais_atendimentos()
    assert ranking[0][0] == "Clínica Vida - Florianópolis"
    assert ranking[0][1] == 2
teste("Relatório: clínicas com mais atendimentos", t_relatorio_clinicas)

def t_relatorio_atendimentos_caros_baratos():
    cp, cc, cpr, ct, ca, cpro, cpag = setup_relatorios()
    resultado = ca.relatorio_atendimentos_mais_caros_baratos()
    totais_caros = [a.calcular_valor_total() for a in resultado["mais_caros"]]
    totais_baratos = [a.calcular_valor_total() for a in resultado["mais_baratos"]]
    assert totais_caros == sorted(totais_caros, reverse=True)
    assert totais_baratos == sorted(totais_baratos, reverse=True)
teste("Relatório: atendimentos mais caros e mais baratos", t_relatorio_atendimentos_caros_baratos)

def t_relatorio_procedimentos_populares():
    cp, cc, cpr, ct, ca, cpro, cpag = setup_relatorios()
    ranking = cpro.relatorio_mais_populares()
    assert ranking[0][0] == "Eletrocardiograma"
    assert ranking[0][1] == 2
teste("Relatório: procedimentos mais populares", t_relatorio_procedimentos_populares)

def t_relatorio_procedimentos_caros_baratos():
    cp, cc, cpr, ct, ca, cpro, cpag = setup_relatorios()
    resultado = cpro.relatorio_mais_caros_baratos()
    custos_caros = [p.calcular_custo() for p in resultado["mais_caros"]]
    assert custos_caros == sorted(custos_caros, reverse=True)
teste("Relatório: procedimentos mais caros e mais baratos", t_relatorio_procedimentos_caros_baratos)

espera_excecao("Relatório sem dados lança ValueError", ValueError,
    lambda: ControladorAtendimento(None, None, None, None).relatorio_clinicas_mais_atendimentos())


# ══════════════════════════════════════════════════════════════════════════════
# RESULTADO FINAL
# ══════════════════════════════════════════════════════════════════════════════
print(f"\n{'═'*45}")
print(f"  RESULTADO: {PASSOU} passou(aram) | {FALHOU} falhou(aram)")
print(f"{'═'*45}\n")