import random
import string

random.seed(19395)

lista = [''.join(random.choice(string.ascii_lowercase) for i in range(2)) for i in range(300)]
x = X('o')
y = X('o')
z = X('o')
print(x.obter_contagem_string(lista,x.y()))
print(x.y())
print(y.y())
print(z.y())
print(type(x.y()))
x.z('y')
y.z('p')
print(x.y())
print(y.y())
print(z.y())
print(type(y))