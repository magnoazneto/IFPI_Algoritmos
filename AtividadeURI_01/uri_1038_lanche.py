def main():
	entradas = input().split(' ')
	codigo = int(entradas[0])
	quantidade = int(entradas[1])
	if codigo == 1:
		total = quantidade * 4.00
	elif codigo == 2:
		total = quantidade * 4.50
	elif codigo == 3:
		total = quantidade * 5.00
	elif codigo == 4:
		total = quantidade * 2.00
	elif codigo == 5:
		total = quantidade * 1.50
	print('Total: R$ {:.2f}'.format(total))


main()