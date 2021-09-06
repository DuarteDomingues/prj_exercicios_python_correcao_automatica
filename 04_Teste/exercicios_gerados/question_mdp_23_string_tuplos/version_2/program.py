import random
import string

random.seed(2701)

lista_strings = []

for i in range(1225):
	lista_strings.append(''.join([random.choice(string.ascii_lowercase) for i in range(7)]))


print((645, [911, 264], (389, 925, 354), 'onfaoi')[-1][-1])
print((645, [911, 264], (389, 925, 354), 'onfaoi')[-2][-1])
print((645, [911, 264], (389, 925, 354), 'onfaoi')[-3][0])
print((645, [911, 264], (389, 925, 354), 'onfaoi')[1][-1])