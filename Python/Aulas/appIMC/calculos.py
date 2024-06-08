def lerNumero(mens):
    numero = 0
    while numero == 0:
        try:
            numero = float(input(mens))
        except:
            numero = 0
    return numero


def getClassificacao(imc):
    classificacao = ""
    if imc <= 18.5:
        classificacao = "MAGREZA"
    elif imc <= 24.5:
        classificacao = "NORMAL"
    elif imc <= 29.9:
        classificacao = "SOBREPESO"
    elif imc <= 39.9:
        classificacao = "OBESIDADE"
    else:
        classificacao = "OBESIDADE GRAVE"
    return classificacao
