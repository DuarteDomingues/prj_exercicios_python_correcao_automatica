class N:

	def __init__(self, t, u):
		self.t = t
		self.u = u
		return self

	def n(self):
		return self.t + self.u
		
n = N(39, 3)
print(n.n())