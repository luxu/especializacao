from funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, ctps, nome, nhtrab, vlrhora, adic):
        super().__init__(ctps, nome, nhtrab, vlrhora)
        self.adic=adic
    
    def calcSalario(self): #override
        return super().calcSalario()*(1+(self.adic/100))
