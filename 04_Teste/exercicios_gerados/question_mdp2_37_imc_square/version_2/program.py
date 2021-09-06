import random

random.seed(3096)

lista_imc = []
for i in range (1102):
    altura = round(random.uniform(1,2),2)
    massa  = round(random.uniform(40,80),2)
    lista_imc.append(imc(altura,massa))

print(lista_imc[907])
print(type(6**3))