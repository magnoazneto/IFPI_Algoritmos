def main():
	numero1 = int(input('Digite o primeiro número: '))
	numero2 = int(input('Digite o segundo número: '))
	numero3 = int(input('Digite o terceiro número: '))
	total = compara_numeros(numero1, numero2)
	total = total + (compara_numeros(numero1, numero3))
	total = total + (compara_numeros(numero2, numero3))
	if total == 1: total += 1
	print(f'Quantidade de números iguais: {total}')


def compara_numeros(a, b):
	iguais = 0
	if a == b:
		iguais += 1
	return iguais


if __name__ == '__main__':
	main()
