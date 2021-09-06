import random
import string

random.seed(3794)

lista_strings = []

for i in range(1575):
	lista_strings.append(''.join([random.choice(string.ascii_lowercase) for i in range(7)]))


print((321, [712, 837], (198, 887, 48), 'i07g1a')[-1][-1])
print((321, [712, 837], (198, 887, 48), 'i07g1a')[-2][-1])
print((321, [712, 837], (198, 887, 48), 'i07g1a')[-3][0])
print((321, [712, 837], (198, 887, 48), 'i07g1a')[1][-1])

print(lista_strings[141])