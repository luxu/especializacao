from candidato import Candidato
from urna import Urna

if __name__ == "__main__":
    urna = Urna(5)
    urna.setTipoDeEleicao('Eleição para o DA')
    u1 = urna.adicCandidato(Candidato('Pele', 10, 'MDB'))
    u2 = urna.adicCandidato(Candidato('Garrincha', 7, 'PL'))
    u3 = urna.adicCandidato(Candidato('Maradona', 33, 'Rede Sustentabilidade'))
    u4 = urna.adicCandidato(Candidato('Messi', 19, 'Republicanos'))
    u5 = urna.adicCandidato(Candidato('Mbappe', 14, 'Conservador'))
    urna.votar(10)
    urna.votar(33)
    urna.votar(7)
    urna.votar(10)
    urna.votar(33)
    urna.votar(33)
    urna.votar(19)
    urna.votar(19)
    urna.emiteBoletimDaUrna()
