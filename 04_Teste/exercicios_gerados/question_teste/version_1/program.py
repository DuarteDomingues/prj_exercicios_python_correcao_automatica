seed = 322119
def pseudo_random_integer(min_int, max_int):
    global seed
    seed = (16807*seed) % 2147483647
    return int(min_int + (max_int - min_int) * seed / 2147483646)

s = []
for m in range(29005):
    s.append(pseudo_random_integer(617, 3305))