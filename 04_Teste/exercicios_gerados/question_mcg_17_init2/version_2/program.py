class L:

	def __init__(self, t, m):
		self.t = t
		self.m = m
		return self

	def l(self):
		return self.t + self.m
		
l = L(38, 22)
print(l.l())