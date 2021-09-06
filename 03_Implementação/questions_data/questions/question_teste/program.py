seed = 123456
def pseudo_random_integer(min_int, max_int):
    global seed
    seed = (16807*seed) % 2147483647
    return int(min_int + (max_int - min_int) * seed / 2147483646)

a = []
for n in range(1000):
    a.append(pseudo_random_integer(100, 200))