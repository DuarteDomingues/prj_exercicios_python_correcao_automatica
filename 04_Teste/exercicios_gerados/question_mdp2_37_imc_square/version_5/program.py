import random

random.seed(2232)

lista_imc = []
for i in range (1608):
    altura = round(random.uniform(1,2),2)
    massa  = round(random.uniform(40,80),2)
    lista_imc.append(imc(altura,massa))

print(lista_imc[733])
print(type(7**5))