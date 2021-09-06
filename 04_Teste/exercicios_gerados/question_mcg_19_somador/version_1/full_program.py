import random
random.seed(69214)

class Somador:

	def __init__(self):

		self.__max         = 0
		self.__min         = 0
		self.__total       = 0
		self.__parcelas    = 0
		self.__listas      = 0

	def soma_lista(self, lista):

		contador = 0
		self.__listas+=1

		for valor in lista:

			if valor > self.__max:
				self.__max = valor

			if valor < self.__min:
				self.__min = valor

			
			contador = contador + valor
			#self.__total+= contador
			self.__total+= valor 
			self.__parcelas+= 1

		return contador

	def estatisticas(self):

		print("número de listas somadas = "+str(self.__listas))
		print("número parcelas somadas  = "+str(self.__parcelas))
		print("total somado             = "+str(self.__total))
		print("parcela mínima           = "+str(self.__min))
		print("parcela máxima           = "+str(self.__max))


somador = Somador()
print(somador.soma_lista([random.randint(14,273), random.randint(24,121), random.randint(24,140)]))
print(somador.soma_lista([-1*random.randint(1345,5031), -2*random.randint(1189, 6392)]))
print(somador.soma_lista([random.randint(14,156), random.randint(37,297)]))
somador.estatisticas()


somador2 = Somador()
print(somador2.soma_lista([random.randint(15,171), random.randint(28,248)]))
print(somador2.soma_lista([-1*random.randint(1401,6538), -2*random.randint(1691, 5503), -3*random.randint(1283,7453)]))
print(somador2.soma_lista([random.randint(25,176), random.randint(36,329), random.randint(7,159), random.randint(5,313)]))
somador2.estatisticas()