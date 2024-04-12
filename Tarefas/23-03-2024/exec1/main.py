"""
1) [variáveis e operadores] Desenvolva um programa que calcule a distância entre dois pontos no plano.
 Os valores dos pontos devem ser informados pelo usuário.
FÓRMULA:
dAB = (((XB-XA)**2+(YB-YA)**2))**0.5
"""
import os
from funcoes import (
    validaERetornaB,
    digitouNumero,
    calcArea
)



if __name__ == "__main__":
    os.system("cls")
    xA = digitouNumero('xA')
    xB = digitouNumero('xB')
    xB = validaERetornaB(xA, xB)

    yA = digitouNumero('yA')
    yB = digitouNumero('yB')
    yB = validaERetornaB(yA, yB)

    resultado = calcArea(xA, xB, yA, yB)
    print(f"A distância entre os pontos ({xA},{xB}) e ({yA},{yB}) é {resultado}.")
