import random
import string

random.seed(30)

lista = [''.join(random.choice(string.ascii_lowercase) for i in range(2)) for i in range(300)]
x = X('a')
y = X('a')
z = X('a')
print(x.obter_contagem_string(lista,x.y()))
print(x.y())
print(y.y())
print(z.y())
print(type(x.y()))
x.z('b')
y.z('c')
print(x.y())
print(y.y())
print(z.y())
print(type(y))