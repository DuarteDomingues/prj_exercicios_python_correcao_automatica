class X:

    def __init__(self, x):
        
        print('construtor: INICIO')
        print('construtor: criacao de um objeto da classe X')
        print('construtor: definicao do atributo x')
        print('construtor: inicializao do atributo x com o valor: ' + str(x))
        self.x = x
        print('construtor: FIM')

    def y(self):

        print('lol y: INICIO')
        print('lol y: execucao do lol y')
        print('lol y: no objeto do tipo X com atributo x: ' + str(self.x))
        print('lol y: FIM')
        return self.x
    
x = X(1)
y = X(2)
x.y()
y.y()
z = X(3)
print(type(y))