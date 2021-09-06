class A:

def __init__(self):
	self.a = 0

def get(self):
	return self.a
	
x = A()
y = x.get()
print(y)