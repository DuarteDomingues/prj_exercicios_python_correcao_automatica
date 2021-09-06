class S:

    def __init__(self, s):
        
        print('construtor: INÍCIO')
        print('construtor: criação de um objeto da classe S')
        print('construtor: definição do atributo s')
        print('construtor: inicialização do atributo s com o valor: ' + str(s))
        self.s = s
        print('construtor: FIM')

    def h(self):

        print('método y: INÍCIO')
        print('método y: execução do método y')
        print('método y: no objeto do tipo s com atributo s: ' + str(self.s))
        print('método y: FIM')
        return self.s
    
s = S(2)
h = S(21)
s.h()
h.h()
e = S(7)
print(type(h))