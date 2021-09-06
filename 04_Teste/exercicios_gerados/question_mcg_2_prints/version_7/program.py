class U:

    def __init__(self, u):
        
        print('construtor: INÍCIO')
        print('construtor: criação de um objeto da classe U')
        print('construtor: definição do atributo u')
        print('construtor: inicialização do atributo u com o valor: ' + str(u))
        self.u = u
        print('construtor: FIM')

    def i(self):

        print('método y: INÍCIO')
        print('método y: execução do método y')
        print('método y: no objeto do tipo u com atributo u: ' + str(self.u))
        print('método y: FIM')
        return self.u
    
u = U(45)
i = U(6)
u.i()
i.i()
b = U(12)
print(type(i))