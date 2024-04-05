from pessoa import Pessoa


class Candidato(Pessoa):
    def __init__(self, nome, numero, partido='PL'):
        super().__init__(nome, numero)
        self.partido = partido

    def __str__(self):
        return f'{self.nome}-{self.numero}-{self.partido}'
