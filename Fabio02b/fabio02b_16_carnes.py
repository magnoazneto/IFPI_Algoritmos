def main():
	carne = cartao = 0
	while carne not in range(1, 4):
		print('Tipo de carne:\n1 - Filé\n2 - Alcatra\n3 - Picanha.')
		carne = int(input('Por favor, selecione a carne desejada:\n>> '))
	quantidade = 0
	while quantidade <= 0:
		quantidade = float(input('Quantidade em KG desejada: \n>> '))
	print('Forma de pagamento: ')
	while cartao not in range(1, 3):
		cartao = int(input('1 - Cartão Tabajara.\n2 - A vista.\n>> '))
	nota_fiscal(carne, quantidade, cartao)


def nota_fiscal(carne, quantidade, cartao):
	if carne == 1:
		if quantidade > 5:
			preco = 5.80
		else:
			preco = 4.90
		carne = 'Filé'
	elif carne == 2:
		if quantidade > 5:
			preco = 6.80
		else:
			preco = 5.90
		carne = 'Alcatra'
	else:
		if quantidade > 5:
			preco = 7.80
		else:
			preco = 6.90
		carne = 'Picanha'
	if cartao == 1:
		desconto = (quantidade*preco)*0.05
	else:
		desconto = 0
	valor_total = (quantidade*preco)
	valor_a_pagar = valor_total - desconto
	print('=======================================================')
	print('---------------------- NOTA FISCAL --------------------')
	print('================= HIPERMERCADO TABAJARA ===============')
	print('Tipo de Carne:\t\t\t\t{}'.format(carne))
	print('Quantidade:\t\t\t\t{:.2f}'.format(quantidade))
	print('Valor total:\t\t\t\tR$ {:.2f}'.format(valor_total))
	print('Desconto:\t\t\t\tR$ {:.2f}'.format(desconto))
	print('Total a pagar:\t\t\t\tR$ {:.2f}'.format(valor_a_pagar))
	print('=======================================================')
	print('--------------- AGRADECEMOS A PREFERÊNCIA!-------------')
	print('=======================================================')


if __name__ == '__main__':
	main()