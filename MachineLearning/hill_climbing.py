import math
import random

def funcao(x):
    # 2−2((x−0.1)/0.9) (sin(5πx)6 )
    return 2**(-2*((x-0.1)/0.9)**2)*(math.sin(5*math.pi*x)**6)

def perturbar():
  return random.uniform(-0.1,0.2)

x = random.uniform(0,1)
apt = funcao(x)
maior_apt = -1000
for i in range(5000):
  x2 = perturbar()
  apt = funcao(x2)
  if apt > maior_apt:
    maior_apt = apt
    x = x2
print('Valor de x..: ', x)
print('valor de y..: ',maior_apt)
