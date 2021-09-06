import random
import string

random.seed(91975)

lista_strings = []

for i in range(1130):
	lista_strings.append(''.join([random.choice(string.ascii_lowercase) for i in range(6)]))

print((3, [13, 2], (5, 10, 8),lista_strings[500]))
print((3, [13, 2], (5, 10, 8),lista_strings[500])[1])
print((3, [13, 2], (5, 10, 8),lista_strings[500])[1][1])
print((3, [13, 2], (5, 10, 8),lista_strings[500])[2][2])
print((3, [13, 2], (5, 10, 8),lista_strings[500])[3][3])