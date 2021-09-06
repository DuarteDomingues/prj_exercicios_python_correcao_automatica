def formula_resolvente(a, b, c):

	bx = ((b**2)-(4*a*c))**(1/2)
	bx1 = (-b+bx)/(2*a)
	bx2 = (-b-bx)/(2*a)
	return bx1, bx2



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
d = -1
e = 78
f = -56
raizes2 = formula_resolvente(d, e, f)
raiz_3 = raizes2[0]
raiz_4 = raizes2[1]
print('a equação -1x**2 + 78x -56 = 0 tem as raízes:')
print('x =')
print(raiz_3)
print('e x =')
print(raiz_4)