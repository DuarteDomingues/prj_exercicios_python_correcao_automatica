import random

random.seed(87155)

class Pessoa:

	def __init__(self, nome, altura, peso):
		self.nome = nome
		self.altura = altura
		self.peso = peso

	def get_dados_pessoa(self):
		return [self.nome, self.altura, self.peso]

	def __str__(self):
		return "Nome: "+str(self.get_dados_pessoa()[0])+", com altura: "+str(self.get_dados_pessoa()[1])+" e peso: "+str(self.get_dados_pessoa()[2])
		

nome = random.choice(["Duarte", "Marta", "Miguel", "Massibas", "Diogo", "Madorna", "Rita", "Eduardo", "Pedro", "Margarida", "Beatriz", "Leonor", "Fonseca"])
altura = round(random.uniform(1.28, 1.96), 2)
peso = random.randint(53,89)

p = Pessoa(nome, altura, peso)
print(p)
print(p.get_dados_pessoa())