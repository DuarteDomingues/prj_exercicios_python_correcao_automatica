import random
import string

random.seed(81529)

lista = [''.join(random.choice(string.ascii_lowercase) for i in range(2)) for i in range(300)]
x = X('u')
y = X('u')
z = X('u')
print(x.obter_contagem_string(lista,x.y()))
print(x.y())
print(y.y())
print(z.y())
print(type(x.y()))
x.z('l')
y.z('d')
print(x.y())
print(y.y())
print(z.y())
print(type(y))