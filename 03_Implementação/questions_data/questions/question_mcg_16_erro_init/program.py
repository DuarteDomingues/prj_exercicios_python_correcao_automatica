class Y:

    def init(self, a, b, c):

        self.a = a
        self.b = b
        self.c = c

    def get(self):

        return self.a

y = Y(1, 2, 3)
print(y.get())