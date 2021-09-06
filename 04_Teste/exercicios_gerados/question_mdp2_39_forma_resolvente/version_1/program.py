# x**2 + 4x -21 = 0
a = 1
b = 4
c = -21
raízes = formula_resolvente(a, b, c)
raiz_1 = raízes[0]
raiz_2 = raízes[1]
print('a equação x**2 + 4x -21 = 0 tem as raízes:')
print('x =')
print(raiz_1)
print('e x =')
print(raiz_2)

# -\verb+value1+x**2 + \verb+value2+x -\verb+value3+
d = -9
e = 80
f = -129
raizes2 = formula_resolvente(d, e, f)
raiz_3 = raizes2[0]
raiz_4 = raizes2[1]
print('a equação -9x**2 + 80x -129 = 0 tem as raízes:')
print('x =')
print(raiz_3)
print('e x =')
print(raiz_4)