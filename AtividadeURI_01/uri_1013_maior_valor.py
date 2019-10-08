def main():
	numeros = input().split()
	a = int(numeros[0])
	b = int(numeros[1])
	c = int(numeros[2])
	print('{} eh o maior'.format(maior(a, b, c)))


def maior(n1, n2, n3):
	if n1 > n2:
	    maior = n1
	    menor = n2
	else:
	    maior = n2
	    menor = n1

	if n3 > maior:
	    maior = n3
	if n3 < menor:
	    menor = n3
	return maior


main()