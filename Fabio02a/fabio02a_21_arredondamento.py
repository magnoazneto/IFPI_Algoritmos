def main():
	numero = float(input('Digite um valor para ser arredondado com até 1 \
casa decimal: '))
	arredondamento(numero)


def arredondamento(numero):
	if ((numero*10) % 10) >= 5:
		numero = int(numero) + 1
		print(numero)
	else:
		numero = int(numero) 
		print(numero)


if __name__ == '__main__':
	main()