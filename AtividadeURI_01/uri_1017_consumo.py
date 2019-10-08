def main():
	TEMPO = int(input())
	VEL_MEDIA = int(input())
	DISTANCIA_PERCORRIDA = TEMPO * VEL_MEDIA
	COMBUSTIVEL = DISTANCIA_PERCORRIDA / 12
	print('{:.3f}'.format(COMBUSTIVEL))


main() 