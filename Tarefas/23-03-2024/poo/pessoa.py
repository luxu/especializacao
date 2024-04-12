class Pessoa:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def __str__(self):
        return f'{self.nome}-{self.numero}'
