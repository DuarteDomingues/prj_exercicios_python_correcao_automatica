class Q:

    def init(self, u, o, e):

        self.u = u
        self.o = o
        self.e = e

    def get(self):

        return self.u

q = Q(47, 7, 2)
print(q.get())