class H:

    def __init__(self, h):
        
        print('construtor: INÍCIO')
        print('construtor: criação de um objeto da classe H')
        print('construtor: definição do atributo h')
        print('construtor: inicialização do atributo h com o valor: ' + str(h))
        self.h = h
        print('construtor: FIM')

    def f(self):

        print('método y: INÍCIO')
        print('método y: execução do método y')
        print('método y: no objeto do tipo h com atributo h: ' + str(self.h))
        print('método y: FIM')
        return self.h
    
h = H(9)
f = H(38)
h.f()
f.f()
p = H(41)
print(type(f))