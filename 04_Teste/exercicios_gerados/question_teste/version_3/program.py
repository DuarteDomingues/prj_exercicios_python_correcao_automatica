seed = 991345
def pseudo_random_integer(min_int, max_int):
    global seed
    seed = (16807*seed) % 2147483647
    return int(min_int + (max_int - min_int) * seed / 2147483646)

y = []
for i in range(67567):
    y.append(pseudo_random_integer(881, 2993))