"""
Trabalho institucional para formacao do curso tecnico.
Autor: Joao Carlos Espinato
Contato: +55 28999644083
"""

import sys


def pausar_no_final():
    if sys.stdin.isatty() and sys.stdout.isatty():
        input("\nPressione Enter para sair...")


def main():
    print("Cadastro da portaria do estacionamento")

    nome_estabelecimento = input("Nome do estabelecimento: ").strip()
    numero_placa = input("Numero da placa do carro: ").strip()
    modelo_carro = input("Modelo do carro: ").strip()
    cor_carro = input("Cor do carro: ").strip()

    print("\nInformacoes cadastradas:")
    print(f"Nome do estabelecimento: {nome_estabelecimento}")
    print(f"Numero da placa: {numero_placa}")
    print(f"Modelo do carro: {modelo_carro}")
    print(f"Cor do carro: {cor_carro}")


try:
    main()
except Exception as erro:
    print(f"Erro: {erro}")
finally:
    pausar_no_final()
