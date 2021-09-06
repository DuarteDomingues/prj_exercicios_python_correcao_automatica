import random
import string

random.seed(88820)

lista = [''.join(random.choice(string.ascii_lowercase) for i in range(2)) for i in range(300)]
x = X('d')
y = X('d')
z = X('d')
print(x.obter_contagem_string(lista,x.y()))
print(x.y())
print(y.y())
print(z.y())
print(type(x.y()))
x.z('u')
y.z('y')
print(x.y())
print(y.y())
print(z.y())
print(type(y))