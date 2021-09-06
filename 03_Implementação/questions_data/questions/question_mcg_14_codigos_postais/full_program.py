import random
import string

random.seed(30)

class GestorCodigoPostais:

    def __init__(self, codigos_postais):

        self.codigos_postais = codigos_postais
    
    def validar_codigos_postais(self):
        
        lista_codigos_postais_validos = []
        for i in range (len(self.codigos_postais)):

            if (len(str(self.codigos_postais[i].digitos4))==4) and (len(str(self.codigos_postais[i].digitos3 ))==3) and (self.codigos_postais[i].localidade.isupper()):
                lista_codigos_postais_validos.append(self.codigos_postais[i])
        
        self.codigos_postais = lista_codigos_postais_validos
    
        
    def obter_codigos_postais_por_localidade(self, localidade):
        
        lista_codigos_postais_localidade = []
        for i in range (len(self.codigos_postais)):
            if self.codigos_postais[i].localidade == localidade:
                lista_codigos_postais_localidade.append(self.codigos_postais[i]) 
        
        return lista_codigos_postais_localidade



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

    numero_4_digitos =  random.randint(1,12000)
    numero_3_digitos =  random.randint(1,1100)
    localidade       =  random.choice(list_localidades)
    codigo_postal_i  =  CodigoPostal(numero_4_digitos,numero_3_digitos,localidade)

    lista_codigos_postais.append(codigo_postal_i)


g = GestorCodigoPostais(lista_codigos_postais)
g.validar_codigos_postais()
print(len(g.codigos_postais))
g.codigos_postais[40].print_codigo_postal()
codigos_postais_localidade = g.obter_codigos_postais_por_localidade("OEIRAS_LOCALIDADE")
print(len(codigos_postais_localidade))