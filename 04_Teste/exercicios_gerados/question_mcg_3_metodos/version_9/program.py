import random
import string

random.seed(71310)

lista = [''.join(random.choice(string.ascii_lowercase) for i in range(2)) for i in range(300)]
x = X('x')
y = X('x')
z = X('x')
print(x.obter_contagem_string(lista,x.y()))
print(x.y())
print(y.y())
print(z.y())
print(type(x.y()))
x.z('s')
y.z('i')
print(x.y())
print(y.y())
print(z.y())
print(type(y))