# x**2 + 4x -21 = 0
a = 1
b = 4
c = -21
raizes = formula_resolvente(a, b, c)
raiz_1 = raizes[0]
raiz_2 = raizes[1]
print('a equacao x**2 + 4x -21 = 0 tem as raizes:')
print('x =')
print(raiz_1)
print('e x =')
print(raiz_2)

# -\verb+value1+x**2 + \verb+value2+x -\verb+value3+
d = -20
e = 100
f = -200
raizes2 = formula_resolvente(d, e, f)
raiz_3 = raizes2[0]
raiz_4 = raizes2[1]
print('a equacao -20x**2 + 100x -200 = 0 tem as raizes:')
print('x =')
print(raiz_3)
print('e x =')
print(raiz_4)