import string

seed = 72182

def pseudo_random_integer(min_int, max_int):
    global seed
    seed = (16807*seed) % 2147483647
    return int(min_int + (max_int - min_int) * seed / 2147483646)



class UmaClasse():

	def __init__(self, um_atributo):

		self.__um_atributo = um_atributo

	def um_metodo(self):

		return self.__um_atributo[0:6]

	def gerar_lista_aleatoria(self):

		strings_aleatorias = []

		for i in range(2165):

			strings_aleatorias.append(self.um_metodo()[pseudo_random_integer(0, 5)])

		return strings_aleatorias


string_completa = string.ascii_lowercase+string.ascii_uppercase
string_aleatoria = ''.join([string_completa[pseudo_random_integer(14,31)] for i in range(2165)])
lista_numeros_aleatorio = [pseudo_random_integer(10000,99999) for i in range(2165)]

objeto1 = UmaClasse(string_aleatoria)
objeto2 = UmaClasse(lista_numeros_aleatorio)

print(objeto1.gerar_lista_aleatoria()[26])
print(objeto2.gerar_lista_aleatoria()[10])

l = objeto2
g = l.um_metodo()
print(g)

l = objeto1
g= l.um_metodo()
print(g)
print(type(l))
print(type(g))