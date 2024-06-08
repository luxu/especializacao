from funcoes import (
    linhaTracejada,
    jogo,
    MENSAGEM
)

if __name__ == "__main__":
    numeroChutes = 3
    comecarJogo = input(MENSAGEM.get('INCIAR'))
    print(linhaTracejada())
    if comecarJogo.upper() == 'S':
        jogo(numeroChutes)
    else:
        print(MENSAGEM.get('DESPEDIDA'))
