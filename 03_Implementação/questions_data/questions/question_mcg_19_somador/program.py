import random

random.seed(100)

class Somador:

	def __init__(self):

		self.__max         = 0
		self.__min         = 0
		self.__total       = 0
		self.__parcelas    = 0
		self.__listas      = 0

	def estatisticas(self):

		print("numero de listas somadas = "+str(self.__listas))
		print("numero parcelas somadas = "+str(self.__parcelas))
		print("total somado = "+str(self.__total))
		print("parcela minima = "+str(self.__min))
		print("parcela maxima = "+str(self.__max))