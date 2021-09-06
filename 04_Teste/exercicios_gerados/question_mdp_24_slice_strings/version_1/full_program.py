import random
import string

random.seed(2596)

lista_strings = []

for i in range(1008):
	lista_strings.append(''.join([random.choice(string.ascii_lowercase+string.ascii_uppercase) for i in range(3)]))

print(lista_strings[137])

print('hello python world!')
print('hello python world!'[5:10])
print('hello python world!'[5:11])
print('hello python world!'[5:-6])
print('hello python world!'[-12:-6])
print('hello python world!'[:-6])
print('hello python world!'[5:])