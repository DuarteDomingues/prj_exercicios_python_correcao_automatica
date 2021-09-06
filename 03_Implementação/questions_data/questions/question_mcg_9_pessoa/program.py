import random

random.seed(100)

class Pessoa:

	def __str__(self):
		return "Nome: "+str(self.get_dados_pessoa()[0])+", com altura: "+str(self.get_dados_pessoa()[1])+" e peso: "+str(self.get_dados_pessoa()[2])
		

nome = random.choice(["Eduardo", "Margarida", "Marta", "Massibas", "Leonor", "Diogo", "Madorna", "Duarte", "Pedro", "Miguel", "Beatriz", "Rita", "Fonseca"])
altura = round(random.uniform(1.5, 2.2), 2)
peso = random.randint(30,120)

p = Pessoa(nome, altura, peso)
print(p)
print(p.get_dados_pessoa())