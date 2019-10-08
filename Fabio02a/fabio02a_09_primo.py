def main():
	numero = int(input('Digite um número: '))
	print('O número é primo!') if testa_primo(numero) else print('O número não é primo.')


def testa_primo(numero):
	total = 0
	for count in range(1, numero+1):
		if numero % count == 0:
			total += 1
	return True if total == 2 else False


if __name__ == '__main__':
	main()