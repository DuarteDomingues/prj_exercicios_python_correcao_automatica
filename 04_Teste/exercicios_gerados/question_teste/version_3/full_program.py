seed = 991345
def pseudo_random_integer(min_int, max_int):
    global seed
    seed = (16807*seed) % 2147483647
    return int(min_int + (max_int - min_int) * seed / 2147483646)

y = []
for i in range(67567):
    y.append(pseudo_random_integer(881, 2993))

answer_1_true = y[318]
answer_2_true = y[1119]
answer_3_true = y[1172]
answer_4_true = y[861]
answer_5_true = y[1275]

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
