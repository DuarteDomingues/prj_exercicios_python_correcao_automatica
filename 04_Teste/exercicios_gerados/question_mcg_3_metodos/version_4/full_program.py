import string
import random

random.seed(81529)

class X:

	def __init__(self, x):

		self.x = x

	def y(self):

		return self.x

	def z(self, y):
		
		self.x = y
    
	def obter_contagem_string(self, lista, letra):
		count=0
		for i in lista:
			if i[0] == letra:
				count  = count+1
			if i[1] == letra:
				count  = count+1
		return count

    
 
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