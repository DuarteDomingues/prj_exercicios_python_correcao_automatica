import random
import string

random.seed(3773)

lista_strings = []

for i in range(1921):
	lista_strings.append(''.join([random.choice(string.ascii_lowercase) for i in range(7)]))


print((191, [233, 318], (584, 515, 936), 'a9qi6u')[-1][-1])
print((191, [233, 318], (584, 515, 936), 'a9qi6u')[-2][-1])
print((191, [233, 318], (584, 515, 936), 'a9qi6u')[-3][0])
print((191, [233, 318], (584, 515, 936), 'a9qi6u')[1][-1])