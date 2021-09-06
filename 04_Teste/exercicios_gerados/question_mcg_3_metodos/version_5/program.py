import random
import string

random.seed(36015)

lista = [''.join(random.choice(string.ascii_lowercase) for i in range(2)) for i in range(300)]
x = X('z')
y = X('z')
z = X('z')
print(x.obter_contagem_string(lista,x.y()))
print(x.y())
print(y.y())
print(z.y())
print(type(x.y()))
x.z('d')
y.z('x')
print(x.y())
print(y.y())
print(z.y())
print(type(y))