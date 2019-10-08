def main():
	DISTANCIA = int(input())
	COMBUSTIVEL = float(input())
	CONSUMO = DISTANCIA / COMBUSTIVEL
	print('{:.3f} km/l'.format(CONSUMO))


main() 