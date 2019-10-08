def main():
	numero1 = int(input('Digite o primeiro número: '))
	numero2 = int(input('Digite o segundo número: '))
	numero3 = int(input('Digite o terceiro número: '))
	maior = maior_valor(numero1, numero2, numero3)
	menor = menor_valor(numero1, numero2, numero3)
	print(f'O maior numero é: {maior}')
	print(f'O menor número é: {menor}')


def maior_valor(n1, n2, n3):
	if n1 > n2:
	    maior = n1
	else:
	    maior = n2
	if n3 > maior:
	    maior = n3
	return maior
	

def menor_valor(n1, n2, n3):
	if n1 > n2:
	    menor = n2
	else:
	    menor = n1
	if n3 < menor:
	    menor = n3
	return menor


if __name__ == '__main__':
	main()