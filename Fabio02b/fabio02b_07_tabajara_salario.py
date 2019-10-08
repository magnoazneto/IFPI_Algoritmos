def main():
	salario = float(input('Digite o salário do colaborador: '))
	calcula_reajuste(salario)


def calcula_reajuste(salario):
	if salario <= 280 and salario > 0:
		reajuste = 0.2
	elif salario <= 700:
		reajuste = 0.15
	elif salario <= 1500:
		reajuste = 0.10
	elif salario > 1500:
		reajuste = 0.05
	else:
		print('O salário deve ser um valor maior ou igual a 1 ')		

	print('> Salário antes do reajuste: {}'.format(salario))
	print('> Percentual de aumento aplicado: {}%'.format(int(reajuste*100)))
	print('> Valor do aumento: R$ {:.2f}'.format(salario*reajuste))
	print('> Novo salário: R$ {:.2f}'.format(salario + (salario*reajuste)))


if __name__ == '__main__':
	main()