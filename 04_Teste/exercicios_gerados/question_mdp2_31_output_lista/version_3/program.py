def r(e):
    return e + 102
def p(e):
    e[0] = e[1]
z = [r(1), r(2)]
p(z)
print(z)