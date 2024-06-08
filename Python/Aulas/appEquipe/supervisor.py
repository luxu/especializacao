from funcionario import Funcionario

class Supervisor(Funcionario):
    def __init__(self, ctps, nome, nhtrab, vlrhora, ds, vs):
        super().__init__(ctps, nome, nhtrab, vlrhora)
        self.ds=ds
        self.vs=vs
        
    def calcSalario(self):
        return super().calcSalario()+self.ds*self.vs
