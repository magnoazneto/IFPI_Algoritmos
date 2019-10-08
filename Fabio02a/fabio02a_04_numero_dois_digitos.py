def main():
	numero = int(input('Digite um número inteiro de 2 digitos: '))
	if compara_numeros(numero) == True:
		print('A dezena é igual a unidade.')
	else:
		print('A dezena é diferente da unidade.')


def compara_numeros(numero):
	if numero < 0:
		numero = numero * (-1)
	dezena = numero // 10
	unidade = numero % 10
	return True if dezena == unidade else False


if __name__ == '__main__':
	main()