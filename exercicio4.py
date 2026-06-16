"""
Trabalho institucional para formacao do curso tecnico.
Autor: Joao Carlos Espinato
Contato: +55 28999644083
"""

import sys

DISTANCIA_NATAL_SAO_PAULO_KM = 2970.0


def ler_velocidade():
    valor = input("Digite a velocidade do veiculo em km/h: ").strip().replace(",", ".")
    velocidade = float(valor)

    if velocidade <= 0:
        raise ValueError("A velocidade precisa ser maior que zero.")

    return velocidade


def pausar_no_final():
    if sys.stdin.isatty() and sys.stdout.isatty():
        input("\nPressione Enter para sair...")


def main():
    velocidade = ler_velocidade()
    tempo_total_horas = DISTANCIA_NATAL_SAO_PAULO_KM / velocidade

    dias = int(tempo_total_horas // 24)
    horas_restantes = int(tempo_total_horas % 24)
    minutos = round((tempo_total_horas - int(tempo_total_horas)) * 60)

    if minutos == 60:
        minutos = 0
        horas_restantes += 1

    if horas_restantes == 24:
        horas_restantes = 0
        dias += 1

    print("\nResultado da viagem:")
    print(f"Distancia considerada: {DISTANCIA_NATAL_SAO_PAULO_KM:.0f} km")
    print(f"Velocidade informada: {velocidade:.2f} km/h")
    print(f"Tempo estimado: {tempo_total_horas:.2f} horas")
    print(f"Tempo aproximado: {dias} dia(s), {horas_restantes} hora(s) e {minutos} minuto(s)")


try:
    main()
except Exception as erro:
    print(f"Erro: {erro}")
finally:
    pausar_no_final()
