def main():
	ENTRADAS_1 = input().split(' ')
	X1 = float(ENTRADAS_1[0])
	Y1 = float(ENTRADAS_1[1])
	ENTRADAS_2 = input().split(' ')
	X2 = float(ENTRADAS_2[0])
	Y2 = float(ENTRADAS_2[1])
	DISTANCIA = (((X2 - X1)**2) + ((Y2 - Y1)**2)) ** (1/2)
	print('{:.4f}'.format(DISTANCIA))


main() 