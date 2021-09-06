import random
import string

random.seed(79142)

lista_strings = []

for i in range(1278):
	lista_strings.append(''.join([random.choice(string.ascii_lowercase) for i in range(6)]))


print(lista_strings[378])

print((13, [18, 8], (1, 11, 19),lista_strings[500]))
print((13, [18, 8], (1, 11, 19),lista_strings[500])[1])
print((13, [18, 8], (1, 11, 19),lista_strings[500])[1][1])
print((13, [18, 8], (1, 11, 19),lista_strings[500])[2][2])
print((13, [18, 8], (1, 11, 19),lista_strings[500])[3][3])