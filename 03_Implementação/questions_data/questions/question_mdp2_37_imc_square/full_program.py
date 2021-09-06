import random

random.seed(400)

def imc(altura, massa):
    return (round(massa/(altura**2),2))

lista_imc = []
for i in range (1000):

    altura = round(random.uniform(1,2),2)
    massa  = round(random.uniform(40,80),2)
    lista_imc.append(imc(altura,massa))


print(lista_imc[420])
print(type(6**5))