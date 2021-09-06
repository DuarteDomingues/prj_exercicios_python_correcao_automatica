import string

seed = 31450

def pseudo_random_integer(min_int, max_int):
    global seed
    seed = (16807*seed) % 2147483647
    return int(min_int + (max_int - min_int) * seed / 2147483646)



class UmaClasse():

	def gerar_lista_aleatoria(self):

		strings_aleatorias = []

		for i in range(3057):

			strings_aleatorias.append(self.um_metodo()[pseudo_random_integer(0, 5)])

		return strings_aleatorias


string_completa = string.ascii_lowercase+string.ascii_uppercase
string_aleatoria = ''.join([string_completa[pseudo_random_integer(13,35)] for i in range(3057)])
lista_numeros_aleatorio = [pseudo_random_integer(10000,99999) for i in range(3057)]

objeto1 = UmaClasse(string_aleatoria)
objeto2 = UmaClasse(lista_numeros_aleatorio)

print(objeto1.gerar_lista_aleatoria()[39])
print(objeto2.gerar_lista_aleatoria()[34])

e = objeto2
t = e.um_metodo()
print(t)

e = objeto1
t= e.um_metodo()
print(t)
print(type(e))
print(type(t))