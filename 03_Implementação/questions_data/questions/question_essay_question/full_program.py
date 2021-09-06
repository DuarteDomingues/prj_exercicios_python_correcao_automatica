seed = 123456

def random_int(min, max):
    global seed
    seed = (16807*seed) % 2147483647
    return int(min + (max - min)*(seed / 2147483646))

class X:
    
    def __init__(self, x):
        
        self.y = x

    def z(self):

        return self.y

w = []
for n in range(1000):
    w.append(X(random_int(100, 200)))


answer_1_true = w[300].z()

print(answer_1_true)