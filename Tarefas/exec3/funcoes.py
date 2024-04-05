

def ehDecimal(nro):
    if nro.isdecimal():
        return True
    return False

def mesDiaExiste(numero, fim):
    numeros = range(1, fim + 1)
    if numero in numeros:
        return True
    return False
def sData(data):
    listaDosMesesPorExtenso = {
        1: "janeiro",
        2: "fevereiro",
        3: "março",
        4: "abril",
        5: "maio",
        6: "junho",
        7: "julho",
        8: "agosto",
        9: "setembro",
        10: "outubro",
        11: "novembro",
        12: "dezembro"
    }
    dia, mes, ano = data.split(",")
    # NÃO é número
    if not ehDecimal(mes.strip()):
        print("MÊS passado não é número. Reveja!")
        return
    mes = int(mes)
    # Não está entre 1 e 12
    if not mesDiaExiste(mes, 12):
        print(f"Mês {mes} inválido. Tem que ser de 1 a 12. Reveja!")
        return
    # NÃO é número
    if not ehDecimal(dia):
        print("DIA passado não é número. Reveja!")
        return
    dia = int(dia)
    # Não está entre 1 e 31
    if not mesDiaExiste(dia, 31):
        print(f"Dia {dia} inválido. Tem que ser de 1 a 31. Reveja!")
        return
    # NÃO é número
    if not ehDecimal(ano.strip()):
        print("ANO passado não é número. Reveja!")
        return
    ano = int(ano)
    mesPorExtenso = [v for (k, v) in listaDosMesesPorExtenso.items() if k == mes][0]
    print(f"{dia} de {mesPorExtenso} de {ano}")
