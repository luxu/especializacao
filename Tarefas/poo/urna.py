from candidato import Candidato

class Urna:
    def __init__(self, quantidadeDeCandidatos, tipoDeEleicao=""):
        self.quantidadeDeCandidatos = quantidadeDeCandidatos
        self.tipoDeEleicao = tipoDeEleicao
        self.candidatos = []
        self.votos = []

    def setTipoDeEleicao(self, tipoDeEleicao):
        self.tipoDeEleicao = tipoDeEleicao

    def getTipoDeEleicao(self):
        return self.tipoDeEleicao

    def olharQuemNaoRecebeuVotosMasEstaNaListaDeCandidatos(self):
        listaFinal = []
        listaDeCandidatosComVoto = [candidato['candidato'] for candidato in self.votos]
        listaDeCandidatosGeral = [(candidato.nome, candidato.numero) for candidato in self.candidatos]
        for candidato in listaDeCandidatosGeral:
            if candidato[0] not in listaDeCandidatosComVoto:
                listaFinal.append(candidato)
        return listaFinal

    def adicCandidato(self, candidato):
        c = Candidato(
            candidato.nome,
            candidato.numero,
            candidato.partido
        )
        self.candidatos.append(c)
        return True

    def listaCandidatos(self):
        return self.candidatos

    def votar(self, numeroDoCandidato):
        objCandidato = [candidato for candidato in self.listaCandidatos() if candidato.numero == numeroDoCandidato]
        if objCandidato:
            obj_nome = objCandidato[0].nome
            obj_numero = objCandidato[0].numero
            if len(self.votos) == 0:
                self.votos.append({
                    'candidato': obj_nome,
                    'numero': obj_numero,
                    'quantidadeDeVotos': 1
                })
            else:
                candidatoTemVoto = [info for info in self.votos if info['candidato'] == obj_nome]
                if candidatoTemVoto:
                    for info in self.votos:
                        if info['candidato'] == obj_nome:
                            info['quantidadeDeVotos'] += 1
                else:
                    self.votos.append({
                        'candidato': obj_nome,
                        'numero': obj_numero,
                        'quantidadeDeVotos': 1
                    })


    def emiteBoletimDaUrna(self):
        cabecalho = f"****{self.getTipoDeEleicao()}***"
        print(cabecalho)
        somarQuantidadeDeVotosNaEleicao =sum([r['quantidadeDeVotos'] for r in self.votos])
        for candidato in self.votos:
            percentualDeVotos = round(candidato['quantidadeDeVotos'] / somarQuantidadeDeVotosNaEleicao * 100, 2)
            relatorio = f"Candidato {candidato['numero']}: {candidato['candidato']}  {candidato['quantidadeDeVotos']} voto(s) ({percentualDeVotos}%)"
            print(relatorio)
        candidatos = self.olharQuemNaoRecebeuVotosMasEstaNaListaDeCandidatos()
        percentualDeVotos = 0
        for candidato in candidatos:
            relatorio = f"Candidato {candidato[1]}: {candidato[0]} 0 voto(s) ({percentualDeVotos}%)"
            print(relatorio)
