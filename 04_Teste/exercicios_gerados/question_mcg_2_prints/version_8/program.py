class F:

    def __init__(self, f):
        
        print('construtor: INÍCIO')
        print('construtor: criação de um objeto da classe F')
        print('construtor: definição do atributo f')
        print('construtor: inicialização do atributo f com o valor: ' + str(f))
        self.f = f
        print('construtor: FIM')

    def b(self):

        print('método y: INÍCIO')
        print('método y: execução do método y')
        print('método y: no objeto do tipo f com atributo f: ' + str(self.f))
        print('método y: FIM')
        return self.f
    
f = F(46)
b = F(11)
f.b()
b.b()
s = F(33)
print(type(b))