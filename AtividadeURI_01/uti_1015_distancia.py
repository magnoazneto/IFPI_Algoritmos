def main():
	ENTRADAS_1 = float(input()).split(' ')
	X1 = ENTRADAS_1[0]
	Y1 = ENTRADAS_1[1]
	ENTRADAS_Y = float(input()).split(' ')
	X2 = ENTRADAS_2[0]
	Y2 = ENTRADAS_2[1]
	DISTANCIA = (((X2 - X1)**2) + ((Y2 - Y1)**2)) ** (1/2)
	print('{:.4f}'.format(DISTANCIA))


main() 