def main():
	a, b, c = map(float, input().split())
	filtro(a, b, c)


def filtro(a, b, c):
	if a >= b + c or b >= a + c or c >= a + b:
		area = ((a+b)/2)*c
		print('Area =', area)
	else:
		print('Perimetro =', (a+b+c))


main()