from funcionario import Funcionario
from gerente import Gerente
from supervisor import Supervisor

equipe = []
func1 = Funcionario(123,"Haroldo",40,25)
equipe.append(func1)
equipe.append(Funcionario(333,"Valdir",40,9.5))
equipe.append(Gerente(987,"Frank",40,25,25))
equipe.append(Supervisor(777,"Toni",40,25,5,18))

for pessoa in equipe:
    print(pessoa," recebe R$ ",pessoa.calcSalario())
    if isinstance(pessoa, Gerente):
        print(f" com adicional de {pessoa.adic} %")
    if isinstance(pessoa, Supervisor):
        print(f" supervisionou {pessoa.ds} dias")
