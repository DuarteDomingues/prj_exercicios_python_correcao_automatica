import random
import string
from gestor_codigos_postais import GestorCodigoPostais

random.seed(92900)

class CodigoPostal:

    def __init__(self, digitos4, digitos3, localidade):

        self.digitos4             = digitos4
        self.digitos3             = digitos3
        self.localidade           = localidade
        self.separador_digitos    = '-'
        self.separador_localidade = ' '
    
    def print_codigo_postal(self):

        print(f"{self.digitos4}{self.separador_digitos}{self.digitos3}{self.separador_localidade}{self.localidade}")

        

list_localidades = ["LOURES","MAFRA","OEIRAS","CASCAIS","lisboa","ESPINHO","MAIA","Amarante","valongo","OVAR","Pombal","Batalha"]

lista_codigos_postais = []
for i in range (1000):

    numero_4_digitos =  random.randint(1,11837)
    numero_3_digitos =  random.randint(1,1225)
    localidade       =  random.choice(list_localidades)
    codigo_postal_i  =  CodigoPostal(numero_4_digitos,numero_3_digitos,localidade)

    lista_codigos_postais.append(codigo_postal_i)


g = GestorCodigoPostais(lista_codigos_postais)
g.validar_codigos_postais()
print(len(g.codigos_postais))
g.codigos_postais[140].print_codigo_postal()
codigos_postais_localidade = g.obter_codigos_postais_por_localidade("MAIA")
print(len(codigos_postais_localidade))