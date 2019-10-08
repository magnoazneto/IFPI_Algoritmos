def main():
	valor1 = float(input('Primeiro valor: '))
	print('Selecione uma opção:\n\
1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão')
	opcao = int(input('>>> '))
	if opcao not in range(1, 5):
		print('Por favor, digite uma opção válida.')
		main()
	valor2 = float(input('Segundo valor: '))
	calculadora(opcao, valor1, valor2)


def calculadora(operacao, valor1, valor2):
	if operacao == 1:
		print('Soma: {} + {} = {:.2f}'.format(valor1, valor2, (valor1+valor2)))
	elif operacao == 2:
		print('Subtração: {} - {} = {:.2f}'.format(valor1, valor2, (valor1-valor2)))
	elif operacao == 3:
		print('Multiplicação: {} x {} = {:.2f}'.format(valor1, valor2, (valor1*valor2)))
	elif operacao == 4:
		if valor2 == 0:
			print('Impossivel dividir por zero.')
		else:
			print('Divisão: {} / {} = {:.2f}'.format(valor1, valor2, (valor1/valor2)))


if __name__ == '__main__':
	main()