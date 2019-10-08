def main():
	numero1 = int(input('Primeiro número: '))
	numero2 = int(input('Segundo número: '))
	numero3 = int(input('Terceiro número: '))
	numero4 = int(input('Quarto número: '))
	numero5 = int(input('Quinto número: '))
	maior = maior_valor(numero1, numero2, numero3)
	menor = menor_valor(numero1, numero2, numero3)
	maior_final = maior_valor(maior, numero4, numero5)
	menor_final = menor_valor(menor, numero4, numero5)
	print(f'Maior valor: {maior_final}')
	print(f'Menor valor: {menor_final}')


def maior_valor(n1, n2, n3):
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