import random
import string

random.seed(59350)

lista = [''.join(random.choice(string.ascii_lowercase) for i in range(2)) for i in range(300)]
x = X('b')
y = X('b')
z = X('b')
print(x.obter_contagem_string(lista,x.y()))
print(x.y())
print(y.y())
print(z.y())
print(type(x.y()))
x.z('f')
y.z('p')
print(x.y())
print(y.y())
print(z.y())
print(type(y))