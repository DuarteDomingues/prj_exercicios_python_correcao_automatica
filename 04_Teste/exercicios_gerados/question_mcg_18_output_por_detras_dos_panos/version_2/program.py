class Carro:

    def __init__(self, marca, modelo, ano):

        self.marca  = marca
        self.modelo = modelo
        self.__ano  = ano

    def marca_modelo(self):

        print(self.marca + ' ' + self.modelo)
             
k = Carro('Nissan', 'GTR',  2019)
a = Carro('BMW', 'M4', 2010 )

k.marca_modelo()
Carro.marca_modelo(k) 
a.marca_modelo()
Carro.marca_modelo(a)