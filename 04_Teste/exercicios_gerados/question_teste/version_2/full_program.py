seed = 927498
def pseudo_random_integer(min_int, max_int):
    global seed
    seed = (16807*seed) % 2147483647
    return int(min_int + (max_int - min_int) * seed / 2147483646)

w = []
for t in range(69632):
    w.append(pseudo_random_integer(814, 4079))

answer_1_true = w[891]
answer_2_true = w[318]
answer_3_true = w[2390]
answer_4_true = w[435]
answer_5_true = w[2743]

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
