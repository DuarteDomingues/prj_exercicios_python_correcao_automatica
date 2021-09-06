seed = 927498
def pseudo_random_integer(min_int, max_int):
    global seed
    seed = (16807*seed) % 2147483647
    return int(min_int + (max_int - min_int) * seed / 2147483646)

w = []
for t in range(69632):
    w.append(pseudo_random_integer(814, 4079))