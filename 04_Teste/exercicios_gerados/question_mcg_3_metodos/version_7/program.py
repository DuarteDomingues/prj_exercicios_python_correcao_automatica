import random
import string

random.seed(80446)

lista = [''.join(random.choice(string.ascii_lowercase) for i in range(2)) for i in range(300)]
x = X('s')
y = X('s')
z = X('s')
print(x.obter_contagem_string(lista,x.y()))
print(x.y())
print(y.y())
print(z.y())
print(type(x.y()))
x.z('j')
y.z('m')
print(x.y())
print(y.y())
print(z.y())
print(type(y))