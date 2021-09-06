import random
import string

random.seed(1300)

lista_strings = []

for i in range(1901):
	lista_strings.append(''.join([random.choice(string.ascii_lowercase+string.ascii_uppercase) for i in range(3)]))

print(lista_strings[225])

print('hello python world!')
print('hello python world!'[3:8])
print('hello python world!'[3:9])
print('hello python world!'[3:-4])
print('hello python world!'[-10:-4])
print('hello python world!'[:-4])
print('hello python world!'[3:])