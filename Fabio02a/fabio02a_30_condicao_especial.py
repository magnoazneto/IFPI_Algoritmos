def main():
	numero = input('Digite um número de 4 digitos: ')
	condicao = checa_condicao(int(numero))
	if condicao == True:
		print('Condição atentida!')
	else:
		print('Condição não atentida.')


def checa_condicao(numero):
	parte01 = numero // 100
	parte02 = numero % 100
	if ((parte01+parte02)**2) == numero:
		return True
	else:
		return False


if __name__ == '__main__':
	main()