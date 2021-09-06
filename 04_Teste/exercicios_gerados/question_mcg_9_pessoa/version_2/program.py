import random

random.seed(29096)

class Pessoa:

	def __str__(self):
		return "Nome: "+str(self.get_dados_pessoa()[0])+", com altura: "+str(self.get_dados_pessoa()[1])+" e peso: "+str(self.get_dados_pessoa()[2])
		

nome = random.choice(["Eduardo", "Pedro", "Leonor", "Diogo", "Massibas", "Marta", "Miguel", "Beatriz", "Madorna", "Rita", "Fonseca", "Duarte", "Margarida"])
altura = round(random.uniform(1.3, 1.65), 2)
peso = random.randint(44,104)

p = Pessoa(nome, altura, peso)
print(p)
print(p.get_dados_pessoa())