def main():
	numeros = []
	print('Digite 5 números: ')
	for c in range(0, 5):
		valor = int(input())
		numeros.append(valor)
	media = (numeros[0] + numeros[1] + numeros[2] + numeros[3] + numeros[4]) / 5
	print(f'Média dos números: {media}\n\
Números maiores que a média encontrados:')
	for c in range (0, 5):
		if numeros[c] > media:
			print(f'{numeros[c]}', end = '  ')
	print()


if __name__ == '__main__':
	main()