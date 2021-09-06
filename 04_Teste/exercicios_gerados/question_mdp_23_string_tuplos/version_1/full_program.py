import random
import string

random.seed(3971)

lista_strings = []

for i in range(1285):
	lista_strings.append(''.join([random.choice(string.ascii_lowercase) for i in range(7)]))


print((445, [122, 836], (45, 712, 318), 'xrmmdk')[-1][-1])
print((445, [122, 836], (45, 712, 318), 'xrmmdk')[-2][-1])
print((445, [122, 836], (45, 712, 318), 'xrmmdk')[-3][0])
print((445, [122, 836], (45, 712, 318), 'xrmmdk')[1][-1])

print(lista_strings[845])