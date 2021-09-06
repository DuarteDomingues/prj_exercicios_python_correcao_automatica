class Carro:

    def __init__(self, marca, modelo, ano):

        self.marca  = marca
        self.modelo = modelo
        self.__ano  = ano

    def marca_modelo(self):

        print(self.marca + ' ' + self.modelo)
             
k = Carro('Chevrolet', 'Camaro',  2020)
c = Carro('Tesla', 'X', 2008 )

k.marca_modelo()
Carro.marca_modelo(k) 
c.marca_modelo()
Carro.marca_modelo(c)