"""
Trabalho institucional para formacao do curso tecnico.
Autor: Joao Carlos Espinato
Contato: +55 28999644083
"""

import sys
from datetime import date


def ler_inteiro(texto):
    return int(input(texto).strip())


def inteiro_para_romano(numero):
    if numero == 0:
        return "N"

    valores = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    romano = []
    restante = numero

    for valor, simbolo in valores:
        while restante >= valor:
            romano.append(simbolo)
            restante -= valor

    return "".join(romano)


def pausar_no_final():
    if sys.stdin.isatty() and sys.stdout.isatty():
        input("\nPressione Enter para sair...")


def main():
    print("Informe os dados do aluno:")
    nome = input("Nome completo: ").strip()

    print("\nData de nascimento:")
    dia_nascimento = ler_inteiro("Dia: ")
    mes_nascimento = ler_inteiro("Mes: ")
    ano_nascimento = ler_inteiro("Ano: ")

    print("\nData da atividade:")
    dia_atividade = ler_inteiro("Dia: ")
    mes_atividade = ler_inteiro("Mes: ")
    ano_atividade = ler_inteiro("Ano: ")

    data_nascimento = date(ano_nascimento, mes_nascimento, dia_nascimento)
    data_atividade = date(ano_atividade, mes_atividade, dia_atividade)

    idade = ano_atividade - ano_nascimento
    if (mes_atividade, dia_atividade) < (mes_nascimento, dia_nascimento):
        idade -= 1

    if idade < 0:
        raise ValueError("A data da atividade nao pode ser anterior a data de nascimento.")

    idade_romana = inteiro_para_romano(idade)

    print("\nSaida:")
    print(f"Nome do aluno: {nome}")
    print(f"Data da atividade: {data_atividade.strftime('%d/%m/%Y')}")
    print(f"Idade em numeros romanos: {idade_romana}")


try:
    main()
except Exception as erro:
    print(f"Erro: {erro}")
finally:
    pausar_no_final()
