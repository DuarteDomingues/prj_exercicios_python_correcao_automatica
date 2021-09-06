class U:

	def __init__(self, k, x):
		self.k = k
		self.x = x
		return self

	def u(self):
		return self.k + self.x
		
u = U(27, 78)
print(u.u())