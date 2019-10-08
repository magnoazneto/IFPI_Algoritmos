def main():
	numero1 = int(input('Primeiro número: '))
	numero2 = int(input('Segundo número: '))
	numero3 = int(input('Terceiro número: '))
	crescente(numero1, numero2, numero3)


def crescente(n1, n2, n3):
	if n1 > n2:
	    maior = n1
	    menor = n2
	else:
	    maior = n2
	    menor = n1
	if n3 > maior:
		meio = maior
		maior = n3
	elif n3 < menor:
		meio = menor
		menor = n3
	else:
		meio = n3
	print(f'Ordem crescente: {menor}, {meio}, {maior}')


if __name__ == '__main__':
	main()