def main():
	hora_aula1 = int(input('Horas/aula do primeiro professor: '))
	hora_aula2 = int(input('Horas/aula do segundo professor: '))
	valor_hora1 = float(input('Quanto o primeiro professor recebe por hora? '))
	valor_hora2 = float(input('Quanto o segundo professor recebe por hora? '))
	salario1 = hora_aula1 * valor_hora1
	salario2 = hora_aula2 * valor_hora2
	if salario1 > salario2:
		print('O professor 1 ganha mais, com um salário de {:.2f}'.format(salario1))
	elif salario1 < salario2:
		print('O professor 2 ganha mais, com um salário de {:.2f}'.format(salario2))
	else:
		print('Os professores ganham o mesmo salário. Valor: {:.2f}'.format(salario1))


if __name__ == '__main__':
	main()