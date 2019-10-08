def main():
	valor1 = int(input('Primeiro valor: '))
	valor2 = int(input('Segundo valor: '))
	if valor1 % valor2 == 1:
		print((valor1 + valor2) + (valor1 % valor2))
	elif valor1 % valor2 == 2:
		if valor1 % 2 == 0:
			print('O valor 1 é par!')
		else:
			print('O valor 1 é ímpar!')
		if valor2 % 2 == 0:
			print('O valor 2 é par!')
		else:
			print('O valor 2 é ímpar!')
	elif valor1 % valor2 == 3:
		print((valor1 + valor2) * valor1)
	elif valor1 % valor2 == 4:
		if valor2 != 0:
			print((valor1 + valor2) / valor2)
		else:
			print(f'Não foi possível dividir porque o valor 2 é {valor2}')
	else:
		print(f'Quadrado do primeiro: {valor1**2}')
		print(f'Quadrado do segundo: {valor2**2}')
		

if __name__ == '__main__':
	main()