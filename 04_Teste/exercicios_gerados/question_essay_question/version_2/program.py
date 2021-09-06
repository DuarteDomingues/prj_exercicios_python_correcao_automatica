seed = 53482

def random_int(min, max):
    global seed
    seed = (16807*seed) % 2147483647
    return int(min + (max - min)*(seed / 2147483646))

class M:
    
    def __init__(self, m):
        
        self.e = m

    def s(self):

        return self.e

h = []
for d in range(1940):
    h.append(M(random_int(114, 356)))