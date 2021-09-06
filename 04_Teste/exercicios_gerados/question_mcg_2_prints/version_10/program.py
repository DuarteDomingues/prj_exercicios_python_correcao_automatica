class D:

    def __init__(self, d):
        
        print('construtor: INÍCIO')
        print('construtor: criação de um objeto da classe D')
        print('construtor: definição do atributo d')
        print('construtor: inicialização do atributo d com o valor: ' + str(d))
        self.d = d
        print('construtor: FIM')

    def j(self):

        print('método y: INÍCIO')
        print('método y: execução do método y')
        print('método y: no objeto do tipo d com atributo d: ' + str(self.d))
        print('método y: FIM')
        return self.d
    
d = D(28)
j = D(17)
d.j()
j.j()
m = D(30)
print(type(j))