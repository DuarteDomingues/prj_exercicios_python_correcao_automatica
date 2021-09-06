def n(w):
    return w + 955
def c(w):
    w[0] = w[1]
f = [n(1), n(2)]
c(f)
print(f)