import random

random.seed(55130)

class Pessoa:

	def __str__(self):
		return "Nome: "+str(self.get_dados_pessoa()[0])+", com altura: "+str(self.get_dados_pessoa()[1])+" e peso: "+str(self.get_dados_pessoa()[2])
		

nome = random.choice(["Margarida", "Massibas", "Eduardo", "Beatriz", "Pedro", "Diogo", "Miguel", "Rita", "Marta", "Leonor", "Fonseca", "Duarte", "Madorna"])
altura = round(random.uniform(1.2, 2.13), 2)
peso = random.randint(51,134)

p = Pessoa(nome, altura, peso)
print(p)
print(p.get_dados_pessoa())