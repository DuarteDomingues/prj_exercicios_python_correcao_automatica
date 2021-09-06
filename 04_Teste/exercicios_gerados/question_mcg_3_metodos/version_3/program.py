import random
import string

random.seed(62917)

lista = [''.join(random.choice(string.ascii_lowercase) for i in range(2)) for i in range(300)]
x = X('p')
y = X('p')
z = X('p')
print(x.obter_contagem_string(lista,x.y()))
print(x.y())
print(y.y())
print(z.y())
print(type(x.y()))
x.z('z')
y.z('k')
print(x.y())
print(y.y())
print(z.y())
print(type(y))