import math
import random

def funcao(x):
    # 2−2((x−0.1)/0.9) (sin(5πx)6 )
    return 2**(-2*((x-0.1)/0.9)**2)*(math.sin(5*math.pi*x)**6)

def perturbar(temp):
  return random.uniform(-temp,temp)

x = random.uniform(0,1)
apt = funcao(x)
maior_apt = -1000
temp = 0.5
it = 5000
taxa_decaimento = temp/it
for i in range(it):
  x2 = perturbar(temp)
  apt = funcao(x2)
  if apt > maior_apt:
    maior_apt = apt
    x = x2

  temp = temp - taxa_decaimento
print('Valor de x..: ', x)
print('valor de y..: ',maior_apt)
