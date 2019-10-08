def main():
	a = int(input('Digite o primeiro número: '))
	b = int(input('Digite o segundo número: '))
	c = int(input('Digite o terceiro número: '))
	print('{} é o maior'.format(maior(a, b, c)))


def maior(n1, n2, n3):
	if n1 > n2:
	    maior = n1
	else:
	    maior = n2
	if n3 > maior:
	    maior = n3
	return maior


if __name__ == '__main__':
	main()