
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
    

          







#x = CodigoPostal(4350,334,'Porto')
#print(f"{x.digitos4}{x.separador_digitos}{x.digitos3}{x.separador_localidade}{x.localidade}")
