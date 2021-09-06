import random
random.seed(50)

class Numero:

    def generate_random_lists(self, lists_length):
        lista = []
        for i in range (self.valor):
            lista_i = (random.sample(range(1, 40), lists_length))
            lista_ordenada = self.ordenar_lista_decresente(lista_i)
            lista.append(lista_ordenada)
        
        return lista


a = Numero(70)
print (a.generate_random_lists(5)[6][2])