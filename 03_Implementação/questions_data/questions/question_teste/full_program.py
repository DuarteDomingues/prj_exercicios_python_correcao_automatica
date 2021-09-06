seed = 123456
def pseudo_random_integer(min_int, max_int):
    global seed
    seed = (16807*seed) % 2147483647
    return int(min_int + (max_int - min_int) * seed / 2147483646)

a = []
for n in range(1000):
    a.append(pseudo_random_integer(100, 200))

answer_1_true = a[11]
answer_2_true = a[22]
answer_3_true = a[33]
answer_4_true = a[44]
answer_5_true = a[55]

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
