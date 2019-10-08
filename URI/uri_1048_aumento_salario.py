def main():
	salario = float(input())
	reajuste = calcula_reajuste(salario)
	print('Novo salario: {:.2f}'.format(salario + (salario*reajuste)))
	print('Reajuste ganho: {:.2f}'.format(salario*reajuste))
	print('Em percentual: {} %'.format(int(reajuste*100)))


def calcula_reajuste(salario):
	if salario <= 400:
		return 0.15
	elif salario <= 800:
		return 0.12
	elif salario <= 1200:
		return 0.1
	elif salario <= 2000:
		return 0.07
	else:
		return 0.04



main()