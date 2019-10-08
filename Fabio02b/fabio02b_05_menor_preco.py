def main():
	produto1 = float(input('Digite o preço do produto 1: '))
	produto2 = float(input('Digite o preço do produto 2: '))
	produto3 = float(input('Digite o preço do produto 3: '))
	filtra_precos(produto1, produto2, produto3)


def filtra_precos(produto1, produto2, produto3):
	menor = menor_valor(produto1, produto2, produto3)
	print('Compre o produto de preço R$ {:.2f}.'.format(menor))


def menor_valor(n1, n2, n3):
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
	return menor

if __name__ == '__main__':
	main()