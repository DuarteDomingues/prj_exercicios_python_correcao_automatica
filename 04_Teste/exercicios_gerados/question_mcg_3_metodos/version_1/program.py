import random
import string

random.seed(65117)

lista = [''.join(random.choice(string.ascii_lowercase) for i in range(2)) for i in range(300)]
x = X('v')
y = X('v')
z = X('v')
print(x.obter_contagem_string(lista,x.y()))
print(x.y())
print(y.y())
print(z.y())
print(type(x.y()))
x.z('m')
y.z('p')
print(x.y())
print(y.y())
print(z.y())
print(type(y))