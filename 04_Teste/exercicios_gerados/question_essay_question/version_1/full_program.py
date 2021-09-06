seed = 12773

def random_int(min, max):
    global seed
    seed = (16807*seed) % 2147483647
    return int(min + (max - min)*(seed / 2147483646))

class T:
    
    def __init__(self, t):
        
        self.v = t

    def y(self):

        return self.v

x = []
for q in range(1118):
    x.append(T(random_int(174, 350)))


answer_1_true = x[856].y()

print(answer_1_true)