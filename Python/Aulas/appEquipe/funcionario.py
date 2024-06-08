class Funcionario:
    def __init__(self, ctps, nome, nhtrab, vlrhora):
        self.ctps=ctps
        self.nome=nome
        self.nhtrab=nhtrab
        self.vlrhora=vlrhora
        
    def calcSalario(self):
        return self.nhtrab * self.vlrhora
    
    def __str__(self):
        return f"{self.nome} {self.ctps}"
