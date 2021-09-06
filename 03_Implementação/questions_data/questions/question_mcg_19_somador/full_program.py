import random
random.seed(100)

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

		print("numero de listas somadas = "+str(self.__listas))
		print("numero parcelas somadas  = "+str(self.__parcelas))
		print("total somado             = "+str(self.__total))
		print("parcela minima           = "+str(self.__min))
		print("parcela maxima           = "+str(self.__max))


somador = Somador()
print(somador.soma_lista([random.randint(10,101), random.randint(20,200), random.randint(30,300)]))
print(somador.soma_lista([-1*random.randint(1000,5000), -2*random.randint(2000, 8000)]))
print(somador.soma_lista([random.randint(25,150), random.randint(12,350)]))
somador.estatisticas()


somador2 = Somador()
print(somador2.soma_lista([random.randint(13,102), random.randint(14,103)]))
print(somador2.soma_lista([-1*random.randint(80,500), -2*random.randint(90, 600), -3*random.randint(110,700)]))
print(somador2.soma_lista([random.randint(120,800), random.randint(130,900), random.randint(140,1001), random.randint(160,1002)]))
somador2.estatisticas()