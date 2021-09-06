class Carro:

    def __init__(self, marca, modelo, ano):

        self.marca  = marca
        self.modelo = modelo
        self.__ano  = ano

    def marca_modelo(self):

        print(self.marca + ' ' + self.modelo)
             
t = Carro('Fiat', '500',  2010)
n = Carro('Nissan', 'GTR', 2007 )

t.marca_modelo()
Carro.marca_modelo(t) 
n.marca_modelo()
Carro.marca_modelo(n)