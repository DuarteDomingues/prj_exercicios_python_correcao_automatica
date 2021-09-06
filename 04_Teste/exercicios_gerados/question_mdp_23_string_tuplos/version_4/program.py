import random
import string

random.seed(4683)

lista_strings = []

for i in range(1805):
	lista_strings.append(''.join([random.choice(string.ascii_lowercase) for i in range(7)]))


print((421, [643, 163], (141, 534, 115), 'clb30t')[-1][-1])
print((421, [643, 163], (141, 534, 115), 'clb30t')[-2][-1])
print((421, [643, 163], (141, 534, 115), 'clb30t')[-3][0])
print((421, [643, 163], (141, 534, 115), 'clb30t')[1][-1])