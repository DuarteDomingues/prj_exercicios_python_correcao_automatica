import random
random.seed(29242)

def c2f(celsius):

    return round(1.8*celsius +32,2)

def f2c(fahreinheit):

    return round((fahreinheit-32)/1.8,2)

lista_f2c = []
for i in range (1753):

    lista_f2c.append(f2c(round(random.uniform(30,100),2)))

lista_c2f = []
for i in range (1044):

    lista_c2f.append(c2f(round(random.uniform(1,38),2)))

print(lista_c2f[418])
print(lista_f2c[1623])