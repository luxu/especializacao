import csv
import random
import os
import ipdb

class MegasenaClass:
    def __init__(self, linha_de_comando=False):
        self.jogos = []
        self.listaDos30NumerosMaisSorteados = []
        self.linha_de_comando = linha_de_comando
        self.carregar('megasena.csv')

    def carregar(self, filename):
        if self.linha_de_comando:
            os.chdir('backend')
        with open(filename, 'r') as _f:
            self.jogos = list(csv.reader(_f, delimiter=";"))

    def getOcorrencias(self):
        ocorrencias = []
        itens = []
        dicionario = {}
        # line = '-' * 40
        for nro in range(1, 61):
            # print(f"{line} Inicio do número..:{nro} {line}")
            for jogo in self.jogos:
                if jogo[2] == str(nro):
                    concurso = jogo[0]
                    data = jogo[1]
                    item = {
                        'concurso': concurso,
                        'data': data,
                    }
                    itens.append(item)
            # for index, jogo in enumerate(itens):
            #     print(f"Concurso..: {jogo['concurso']}({jogo['data']}) {index + 1}")
            # print(f"{line} Fim do número..:{nro} {line}")
            dicionario['numero'] = nro
            dicionario['qtadeNro'] = len(itens)
            ocorrencias.append(dicionario)
            itens = []
            dicionario = {}
        ocorrencias.sort(key=lambda x: x['qtadeNro'], reverse=True)
        return ocorrencias

    def conferir(self, volante):  # sourcery skip: switch
        # line = '-' * 40
        if len(volante) < 6 or len(volante) > 9:
            return 0, len(volante)
        # jogos = ['39', '9', '11', '54', '7', '57']
        # ['concurso', 'data', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6']
        # ['2707', '02/04/2024', '39', '9', '11', '54', '7', '57']
        numeros_acertados = []
        quantidade_numero_jogo = 0
        data_numeros_acertados = ''
        jogo_numeros_acertados = []
        jogo_e_data_do_acerto = []
        for jogo in self.jogos[1:]:
            for nro in volante:
                if str(nro) in jogo:
                    if nro not in numeros_acertados:
                        numeros_acertados.append(nro)
                    quantidade_numero_jogo += 1
                    jogo_numeros_acertados.append(jogo[0])
                    if len(data_numeros_acertados) == 0:
                        data_numeros_acertados = jogo[1]
            quantidade_numeros_acertados = len(numeros_acertados)
            if quantidade_numeros_acertados > 0:
                if quantidade_numeros_acertados == 6:
                    premiacao = 'SENA'
                    item = {
                        'premiacao': premiacao,
                        'data': data_numeros_acertados
                    }
                    jogo_e_data_do_acerto.append(item)
                elif quantidade_numeros_acertados == 5:
                    premiacao = 'QUINA'
                    item = {
                        'premiacao': premiacao,
                        'data': data_numeros_acertados
                    }
                    jogo_e_data_do_acerto.append(item)
                elif quantidade_numeros_acertados == 4:
                    premiacao = 'QUADRA',
                    item = {
                        'premiacao': premiacao,
                        'data': data_numeros_acertados
                    }
                    jogo_e_data_do_acerto.append(item)
            data_numeros_acertados = []
            jogo_numeros_acertados = []
            quantidade_numero_jogo = 0
            numeros_acertados = []
        # ipdb.set_trace()
        return jogo_e_data_do_acerto

    def sugerirJogo(self):
        lista = [r['nro'] for r in self.listaDos30NumerosMaisSorteados]
        cont = 0
        listaFinal = []
        while cont < 8:
            numeroGerado = random.choice(lista)
            if numeroGerado not in listaFinal:
                listaFinal.append(numeroGerado)
                cont += 1
        return listaFinal
    def numerosMaisSorteados(self):
        for nro in range(1, 61):
            qtde = 0
            for jogo in self.jogos[1:]:
                soNumeros = jogo[2:]
                tranformadoEmIntlambda = lambda l: [int(x) for x in soNumeros]
                listaSoNumeros = tranformadoEmIntlambda(soNumeros)
                if nro in listaSoNumeros:
                    qtde += 1
            item = {
                'nro': nro,
                'qtde': qtde
            }
            self.listaDos30NumerosMaisSorteados.append(item)
            # print(f'Numero {nro} apareceu {qtde} vezes na história')
                # break
        self.listaDos30NumerosMaisSorteados.sort(key=lambda x: x['qtde'], reverse=True)
        self.listaDos30NumerosMaisSorteados = self.listaDos30NumerosMaisSorteados[:30]

    def __str__(self):
        return f'{self.jogos}'
