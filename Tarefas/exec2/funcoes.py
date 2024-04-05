from random import randint

MENSAGEM = {
    "INCIAR": "Gostaria de jogar o JOGO DA ADIVINHAÇÃO? (s/n)",
    "DESPEDIDA": "OK. Podemos jogar mais tarde. Bye, Bye!"
}


def isDecimal(numero):
    while not numero.isdecimal():
        numero = input("O número deve ser um número inteiro. Tente novamente:")
    return int(numero)


def validarNumeroEscolhido(numero):
    numero = isDecimal(numero)
    while numero < 0 or numero > 100:
        numero = input("O número deve estar entre 0 e 100. Tente novamente:")
        numero = isDecimal(numero)
    return numero


def linhaTracejada():
    return "-" * 50


def jogo(numeroChutes):
    jogar = True
    while jogar:
        numeroSorteado = randint(1, 101)
        print("Número sorteado: ", numeroSorteado)
        chute = 0
        dica = []
        while True:
            chute += 1
            if chute > numeroChutes:
                print(f"Fim de jogo. Não há mais chutes. O número sorteado era {numeroSorteado}.")
                print(linhaTracejada())
                break
            numeroEscolhido = validarNumeroEscolhido(input("Escolha um número entre 0 e 100: "))
            if numeroEscolhido == numeroSorteado:
                print(f"Acertou. Foram feito(s) {chute} chute(s) de {numeroChutes} possíveis. Parabéns!")
                print(linhaTracejada())
                break
            elif numeroEscolhido > numeroSorteado:
                if chute >= numeroChutes:
                    continue
                dica = ['ACIMA', 'MENOR']
            elif numeroEscolhido < numeroSorteado:
                if chute >= numeroChutes:
                    continue
                dica = ['ABAIXO', 'MAIOR']
            print(f"O número: {numeroEscolhido} está {dica[0]} tente um número {dica[1]}.")
            print(f"Voce tem {numeroChutes - chute} tentativas para acertar o número.")
            print(linhaTracejada())
        comecarJogo = input(MENSAGEM.get('INCIAR'))
        if comecarJogo.upper() == 'N':
            jogar = False
            print(MENSAGEM.get('DESPEDIDA'))
