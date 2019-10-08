def main():
	opcao = int(input('Digite uma opção (de 1 a 3): '))
	if opcao not in range(1, 4): 
		print('Opção inválida!')
		main()
	numero1 = int(input('Digite um numero de saida da opção 1: '))
	numero2 = int(input('Digite um numero de saida da opção 2: '))
	numero3 = int(input('Digite um numero de saida da opção 3: '))
	menu(opcao, numero1, numero2, numero3)


def menu(opcao, numero1, numero2, numero3):
	if opcao == 1:
		print(numero1)
	elif opcao == 2:
		print(numero2)
	elif opcao == 3:
		print(numero3)
	else:
		print('Opção inválida.')


if __name__ == '__main__':
	main()