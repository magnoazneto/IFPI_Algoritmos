def main():
	valor = int(input('Digite um número para checar: '))
	par_ou_impar(valor)


def par_ou_impar(valor):
	if valor % 2 == 0:
		print('O número é par!')
	else:
		print('O número é ímpar!')


if __name__ == '__main__':
	main()