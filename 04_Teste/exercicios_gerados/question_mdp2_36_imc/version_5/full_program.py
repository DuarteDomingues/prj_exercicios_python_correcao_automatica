import random

random.seed(2602)

def imc(altura, massa):
    return (round(massa/(altura*altura),2))

lista_imc = []
for i in range (1810):

    lista_imc.append(imc(round(random.uniform(1,2),2),round(random.uniform(40,80),2)))


print(lista_imc[632])

