"""
Trabalho institucional para formacao do curso tecnico.
Autor: Joao Carlos Espinato
Contato: +55 28999644083
"""

import sys


def ler_medida(texto):
    valor = input(texto).strip().replace(",", ".")
    return float(valor)


def pausar_no_final():
    if sys.stdin.isatty() and sys.stdout.isatty():
        input("\nPressione Enter para sair...")


def main():
    base = ler_medida("Digite a base do quadrado em cm: ")
    altura = ler_medida("Digite a altura do quadrado em cm: ")

    area = base * altura

    print(f"Area do quadrado: {area:.2f} cm2")


try:
    main()
except Exception as erro:
    print(f"Erro: {erro}")
finally:
    pausar_no_final()
