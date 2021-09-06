class W:

    def init(self, p, e, c):

        self.p = p
        self.e = e
        self.c = c

    def get(self):

        return self.p

w = W(41, 13, 54)
print(w.get())