def main():
	numero = float(input('Digite um número: '))
	if numero > 0:
		print('Número positivo.')
	elif numero == 0:
		print('Número neutro.')
	else:
		print('Número negativo')


if __name__ == '__main__':
	main()