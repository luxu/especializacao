"""
4) [listas de listas, módulos] A tabela de frequência é um recurso estatístico utilizado para classificar e representar
um conjunto de valores. É formada por n informações contendo o limite inferior, o limite superior e a quantidade
de elementos do vetor que são maiores ou iguais ao limite inferior e menores que o limite superior. A diferença
entre o limite superior e o limite inferior de cada registro, também chamada de amplitude, é calculada da seguinte
forma: RoundUp((maior_elemento – menor_elemento)/n). O valor de n é calculado pela raiz quadrada da
quantidade de elementos do vetor. Dado um vetor de números inteiros ordenados, faça uma função que ao receber
este vetor e seu tamanho lógico, gere e retorne uma matriz dinâmica de frequência. RoundUp significa
arredondamento para cima (não é uma função da linguagem Python), mas pode ser representada pela função
math.ceil.
Exemplo de tabela de frequência:
vetor : 2,3,4,6,7,9,10,15,17,18,20,22,25,29,30,31,33,36,37,39,50,53,56,80,96
n: sqrt(25) = 5
amplitude: (96-2)/5 = 18,8 = 19
"""

# from funcoes import (
#     sData
# )
from math import sqrt, ceil
from random import randint

if __name__ == "__main__":
    # vetor = sorted(set([randint(1, 51) for _ in range(25)]))
    # vetor = [6, 13, 18, 24, 25, 27, 31, 39, 42, 45, 50, 51, 52, 58, 60, 62, 62, 80, 83, 88, 91, 92, 95, 96, 99]
    vetor = [2, 3, 4, 6, 7, 9, 10, 15, 17, 18, 20, 22, 25, 29, 30, 31, 33, 36, 37, 39, 50, 53, 56, 80, 96]
    line = "-" * 50

    menor_elemento = vetor[0]
    maior_elemento = vetor[-1]
    tamanho_vetor = len(vetor)
    n = sqrt(tamanho_vetor)
    elemento_n = (maior_elemento - menor_elemento) / n
    amplitude = ceil(elemento_n)

    limite_inferior = []
    vlr = 2
    for nr in vetor:
        if vlr > maior_elemento:
            break
        limite_inferior.append(vlr)
        vlr += amplitude
    limite_superior = []
    for limite in limite_inferior:
        soma_limite = limite + amplitude
        limite_superior.append(soma_limite)
    matriz = []
    for inf, sup in zip(limite_inferior, limite_superior):
        matriz.append([inf, sup])
    quantidadeElementos = []
    for i in range(len(matriz)):
        min = matriz[i][0]
        max = matriz[i][1]
        quantidadeElementos.append(len([infoVetor for infoVetor in vetor if min <= infoVetor < max]))
        # print(quantidadeElementos)
    print(f"------------------| AMPLITUDE..: {amplitude} |------------------")
    print(f"{vetor}")
    print(f" {line}----\n| Limite Inferior  | Limite Superior  | Qtde Elementos |\n|{line}----|")
    for inf, sup, qtd in zip(limite_inferior, limite_superior, quantidadeElementos):
        colunaInferior = f"|        {str(inf).rjust(2, '0')}        "
        colunaSuperior = f"|        {str(sup).rjust(2, '0')}       "
        colunaQuantidade = f"     {str(qtd).rjust(2, '0')}        |"
        print(f"{colunaInferior}{colunaSuperior} | {colunaQuantidade}")
    print(f' {line}----')