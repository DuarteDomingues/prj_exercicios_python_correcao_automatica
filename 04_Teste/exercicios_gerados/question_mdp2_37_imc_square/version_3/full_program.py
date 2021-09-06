import random

random.seed(3886)

def imc(altura, massa):
    return (round(massa/(altura**2),2))

lista_imc = []
for i in range (1351):

    altura = round(random.uniform(1,2),2)
    massa  = round(random.uniform(40,80),2)
    lista_imc.append(imc(altura,massa))


print(lista_imc[915])
print(type(4**7))