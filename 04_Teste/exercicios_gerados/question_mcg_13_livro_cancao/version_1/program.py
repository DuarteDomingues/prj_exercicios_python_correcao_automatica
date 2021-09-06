class Livro:

	def __init__(self, titulo, numero_paginas):

		self.titulo = titulo
		self.numero_paginas = numero_paginas


class Cancao:

	def __init__(self, titulo, duracao):

		self.titulo = titulo
		self.duracao = duracao


x1 = Livro('One Hundred Years of Solitude', 404)
x2 = Cancao('Crawling', 2.514)
x3 = x1
print(x3.titulo)
print(x3.numero_paginas)
x3 = x2
print(x3.titulo)
print(x3.numero_paginas)