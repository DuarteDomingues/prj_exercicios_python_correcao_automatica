class Z:

	def __init__(self, x, y):
		self.x = x
		self.y = y
		return self

	def z(self):
		return self.x + self.y
		
z = Z(10, 20)
print(z.z())