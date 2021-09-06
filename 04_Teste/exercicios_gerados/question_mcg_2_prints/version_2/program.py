class O:

    def __init__(self, o):
        
        print('construtor: INÍCIO')
        print('construtor: criação de um objeto da classe O')
        print('construtor: definição do atributo o')
        print('construtor: inicialização do atributo o com o valor: ' + str(o))
        self.o = o
        print('construtor: FIM')

    def n(self):

        print('método y: INÍCIO')
        print('método y: execução do método y')
        print('método y: no objeto do tipo o com atributo o: ' + str(self.o))
        print('método y: FIM')
        return self.o
    
o = O(24)
n = O(13)
o.n()
n.n()
j = O(37)
print(type(n))