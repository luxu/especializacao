import math


def bEhMenor(A, B):
    return B < A


def validaERetornaB(A, B):
    flag = bEhMenor(A, B)
    # se for False entra no loop e para ser True o valor de B tem que ser menor que o valor de A
    while not flag:
        flag = bEhMenor(A, B)
        if not flag:
            while True:
                try:
                    B = float(input(
                        "Redigite o valor do SEGUNDO ponto pois tem que ser menor que o do PRIMEIRO ponto: ")
                    )
                    break
                except ValueError:
                    print("Y inválido, tente novamente!")
    return B


def calcArea(xA, xB, yA, yB):
    ladoX = (xB - xA) ** 2
    ladoY = (yB - yA) ** 2
    somaXY = ladoX + ladoY
    return math.sqrt(somaXY)


def digitouNumero(letraDaCoordenada):
    ordem = ""
    if letraDaCoordenada[1] == 'A':
        ordem = 'primeiro'
    elif letraDaCoordenada[1] == 'B':
        ordem = 'segundo'
    textoDigite = f'Digite a coordenada {letraDaCoordenada[0].upper()} do {ordem.upper()} ponto'
    while True:
        try:
            numeroDigitado = float(input(f"{textoDigite}: "))
            break
        except ValueError:
            print("X inválido, tente novamente!")
    return numeroDigitado
