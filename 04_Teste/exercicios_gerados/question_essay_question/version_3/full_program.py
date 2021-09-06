seed = 60461

def random_int(min, max):
    global seed
    seed = (16807*seed) % 2147483647
    return int(min + (max - min)*(seed / 2147483646))

class H:
    
    def __init__(self, h):
        
        self.z = h

    def b(self):

        return self.z

y = []
for g in range(1699):
    y.append(H(random_int(115, 369)))


answer_1_true = y[1021].b()

print(answer_1_true)