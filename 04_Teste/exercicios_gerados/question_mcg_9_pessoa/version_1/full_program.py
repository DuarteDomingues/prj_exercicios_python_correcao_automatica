import random

random.seed(55130)

class Pessoa:

	def __init__(self, nome, altura, peso):
		self.nome = nome
		self.altura = altura
		self.peso = peso

	def get_dados_pessoa(self):
		return [self.nome, self.altura, self.peso]

	def __str__(self):
		return "Nome: "+str(self.get_dados_pessoa()[0])+", com altura: "+str(self.get_dados_pessoa()[1])+" e peso: "+str(self.get_dados_pessoa()[2])
		

nome = random.choice(["Margarida", "Massibas", "Eduardo", "Beatriz", "Pedro", "Diogo", "Miguel", "Rita", "Marta", "Leonor", "Fonseca", "Duarte", "Madorna"])
altura = round(random.uniform(1.2, 2.13), 2)
peso = random.randint(51,134)

p = Pessoa(nome, altura, peso)
print(p)
print(p.get_dados_pessoa())