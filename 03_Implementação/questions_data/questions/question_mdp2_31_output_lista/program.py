def f(x):
    return x + 3
def g(x):
    x[0] = x[1]
y = [f(1), f(2)]
g(y)
print(y)