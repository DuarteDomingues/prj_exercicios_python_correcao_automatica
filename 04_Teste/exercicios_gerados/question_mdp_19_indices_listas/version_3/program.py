import random
import string

random.seed(64097)

lista_strings = []

for i in range(1308):
	lista_strings.append(''.join([random.choice(string.ascii_lowercase) for i in range(6)]))

print((12, [7, 8], (10, 11, 2),lista_strings[500]))
print((12, [7, 8], (10, 11, 2),lista_strings[500])[1])
print((12, [7, 8], (10, 11, 2),lista_strings[500])[1][1])
print((12, [7, 8], (10, 11, 2),lista_strings[500])[2][2])
print((12, [7, 8], (10, 11, 2),lista_strings[500])[3][3])