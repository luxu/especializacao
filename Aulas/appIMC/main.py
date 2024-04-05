import json

import calculos

nome = input("Informe seu nome completo ")
listaImc = []
while len(nome) != 0:
    peso = 0
    peso = calculos.lerNumero("Informe seu peso e Kg ")
    altura = calculos.lerNumero("Informe sua altura em metros ")
    imc = peso / altura ** 2
    pessoa = {}
    pessoa['nome'] = nome
    pessoa['imc'] = imc
    listaImc.append(pessoa)
    print(
        "%s, seu IMC é: %.1f, foi classificado com %s"
        % (
            nome.split(" ")[0],
            imc,
            calculos.getClassificacao(imc)
        )
    )
    nome = input("Informe seu nome completo ")
print("imcs calculados")
arq = open("pessoas.txt", "a+")
for e in listaImc:
    arq.write(json.dumps(e) + "\n")
arq.close()
