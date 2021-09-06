import random
import string

random.seed(100)

lista_strings = []

for i in range(1000):
	lista_strings.append(''.join([random.choice(string.ascii_lowercase) for i in range(6)]))

print((4, [5, 600], (7, 8, 9),lista_strings[500]))
print((4, [5, 600], (7, 8, 9),lista_strings[500])[1])
print((4, [5, 600], (7, 8, 9),lista_strings[500])[1][1])
print((4, [5, 600], (7, 8, 9),lista_strings[500])[2][2])
print((4, [5, 600], (7, 8, 9),lista_strings[500])[3][3])