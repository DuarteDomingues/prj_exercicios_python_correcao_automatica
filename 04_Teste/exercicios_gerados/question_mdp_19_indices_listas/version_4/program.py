import random
import string

random.seed(58057)

lista_strings = []

for i in range(1042):
	lista_strings.append(''.join([random.choice(string.ascii_lowercase) for i in range(6)]))

print((1, [13, 18], (11, 10, 15),lista_strings[500]))
print((1, [13, 18], (11, 10, 15),lista_strings[500])[1])
print((1, [13, 18], (11, 10, 15),lista_strings[500])[1][1])
print((1, [13, 18], (11, 10, 15),lista_strings[500])[2][2])
print((1, [13, 18], (11, 10, 15),lista_strings[500])[3][3])