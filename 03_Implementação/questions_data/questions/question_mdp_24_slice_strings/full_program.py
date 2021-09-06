import random
import string

random.seed(100)

lista_strings = []

for i in range(1000):
	lista_strings.append(''.join([random.choice(string.ascii_lowercase+string.ascii_uppercase) for i in range(3)]))

print(lista_strings[65])

print('hello python world!')
print('hello python world!'[6:11])
print('hello python world!'[6:12])
print('hello python world!'[6:-7])
print('hello python world!'[-13:-7])
print('hello python world!'[:-7])
print('hello python world!'[6:])