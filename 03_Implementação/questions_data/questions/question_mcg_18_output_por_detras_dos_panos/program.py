class Carro:

    def __init__(self, marca, modelo, ano):

        self.marca  = marca
        self.modelo = modelo
        self.__ano  = ano

    def marca_modelo(self):

        print(self.marca + ' ' + self.modelo)
             
x = Carro('Fiat', '500',  2007)
y = Carro('Mini', '1000', 2000 )

x.marca_modelo()
Carro.marca_modelo(x) 
y.marca_modelo()
Carro.marca_modelo(y) 