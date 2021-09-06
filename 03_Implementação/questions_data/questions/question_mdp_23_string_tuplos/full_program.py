import random
import string

random.seed(100)

lista_strings = []

for i in range(1000):
	lista_strings.append(''.join([random.choice(string.ascii_lowercase) for i in range(7)]))


print((10, [20, 30], (4, 5, 6), 'abcdef')[-1][-1])
print((10, [20, 30], (4, 5, 6), 'abcdef')[-2][-1])
print((10, [20, 30], (4, 5, 6), 'abcdef')[-3][0])
print((10, [20, 30], (4, 5, 6), 'abcdef')[1][-1])

print(lista_strings[65])