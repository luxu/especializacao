from megasena import MegasenaClass

if __name__ == "__main__":
    megasena = MegasenaClass()
    filename = "megasena.csv"
    # megasena.carregar(filename)
    # 2708 jogos
    ocorrencias = megasena.getOcorrencias()
    jogo = [
        '9',
        '11',
        '23',
        '39',
        '7',
        '54',
        '32',
        '30',
        '57',
    ]
    # flag, erro = megasena.conferir(jogo)
    # if not flag:
    #     print("Jogo invalido...veio com..: ", erro)
    # megasena.numerosMaisSorteados()
    # for numero in megasena.listaDos30NumerosMaisSorteados[:30]:
    #     print(numero)
    # megasena.sugerirJogo()