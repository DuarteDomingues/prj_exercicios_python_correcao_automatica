import random
import string

random.seed(2524)

lista_strings = []

for i in range(1054):
	lista_strings.append(''.join([random.choice(string.ascii_lowercase+string.ascii_uppercase) for i in range(3)]))

print('hello python world!')
print('hello python world!'[2:7])
print('hello python world!'[2:8])
print('hello python world!'[2:-3])
print('hello python world!'[-9:-3])
print('hello python world!'[:-3])
print('hello python world!'[2:])