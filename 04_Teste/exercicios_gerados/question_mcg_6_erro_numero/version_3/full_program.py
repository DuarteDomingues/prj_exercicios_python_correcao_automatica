import random
random.seed(489)

class Numero:

    def __init__(self, valor):

        self.valor = valor
    
    def ordenar_lista_decresente(self, lista):
    
        return sorted(lista, key=None, reverse=True)
    
    def generate_random_lists(self, lists_length):
        lista = []
        for i in range (self.valor):
            lista_i = (random.sample(range(1, 40), lists_length))
            lista_ordenada = self.ordenar_lista_decresente(lista_i)
            lista.append(lista_ordenada)
        
        return lista


g = Numero(145)
print (g.generate_random_lists(5)[130][2])