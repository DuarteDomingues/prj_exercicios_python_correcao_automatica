class W:

    def __init__(self, w):
        
        print('construtor: INÍCIO')
        print('construtor: criação de um objeto da classe W')
        print('construtor: definição do atributo w')
        print('construtor: inicialização do atributo w com o valor: ' + str(w))
        self.w = w
        print('construtor: FIM')

    def m(self):

        print('método y: INÍCIO')
        print('método y: execução do método y')
        print('método y: no objeto do tipo w com atributo w: ' + str(self.w))
        print('método y: FIM')
        return self.w
    
w = W(28)
m = W(15)
w.m()
m.m()
z = W(42)
print(type(m))