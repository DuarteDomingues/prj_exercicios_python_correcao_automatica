def formula_resolvente(a, b, c):

	bx = ((b**2)-(4*a*c))**(1/2)
	bx1 = (-b+bx)/(2*a)
	bx2 = (-b-bx)/(2*a)
	return bx1, bx2