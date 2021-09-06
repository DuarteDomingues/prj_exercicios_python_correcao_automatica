seed = 322119
def pseudo_random_integer(min_int, max_int):
    global seed
    seed = (16807*seed) % 2147483647
    return int(min_int + (max_int - min_int) * seed / 2147483646)

s = []
for m in range(29005):
    s.append(pseudo_random_integer(617, 3305))

answer_1_true = s[708]
answer_2_true = s[476]
answer_3_true = s[348]
answer_4_true = s[1397]
answer_5_true = s[2140]

print(answer_1_true)
print(answer_2_true)
print(answer_3_true)
print(answer_4_true)
print(answer_5_true)
