def main():
	numero = int(input())
	filtro(numero)


def filtro(numero):
	centena = numero // 100
	dezena = (numero // 10)  % 10
	unidade = numero % 10
	if centena >= 1:
		if centena == 1:
			print(f'{centena} centena', end = '')
		else:
			print(f'{centena} centenas', end = '')
	if dezena >= 1:
		if centena > 0 and unidade != 0:
			print(',', end = ' ')
		elif centena > 0:
			print(' e', end= ' ')
		else:
			print('', end = ' ')
		if dezena == 1:
			print(f'{dezena} dezena', end = '')
		elif centena >= 1:
			print(f'{dezena} dezenas', end = '')
	if unidade >= 1:
		if dezena > 0 and centena == 0 or centena > 0 and dezena == 0:
			print(' e', end = ' ')
		elif dezena > 0 or dezena > 0:
			print(',', end = ' ')
		else:
			print('', end = '')
		if unidade == 1:
			print(f'{unidade} unidade', end = '')
		elif centena >= 1:
			print(f'{unidade} unidades', end = '')
	print()


if __name__ == '__main__':
	main()