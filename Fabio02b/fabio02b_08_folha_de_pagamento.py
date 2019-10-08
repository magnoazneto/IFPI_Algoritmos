def main():
	salario_hora = float(input('Digite o valor da sua hora trabalhada: '))
	horas_trabalhadas = float(input('Digite a quantidade de horas trabalhadas: '))
	if (salario_hora*horas_trabalhadas) < 0:
		print('Salário deve ser maior ou igual a 0.')
		main()
	contra_cheque(salario_hora, horas_trabalhadas)

def contra_cheque(salario_hora, horas_trabalhadas):
	salario_bruto = salario_hora * horas_trabalhadas
	if salario_bruto <= 900:
		IR = 0
	elif salario_bruto <= 1500:
		IR = 0.05
	elif salario_bruto <= 2500:
		IR = 0.1
	else:
		IR = 0.2

	print('-----'*6)
	print('----- CONTRACHEQUE MENSAL -----')
	print('> SALÁRIO BRUTO: ({} x {})\tR$ {:.2f}'.format(salario_hora,\
horas_trabalhadas, salario_bruto))
	print('> (-) IR ({}%):\t\tR$ {:.2f}'.format(IR*100, salario_bruto*IR))
	print('> (-) INSS (10%):\t\tR$ {:.2f}'.format(salario_bruto*0.10))
	print('> FGTS (11%):\t\t\tR$ {:.2f}'.format(salario_bruto*0.11))
	total_descontos = salario_bruto*IR + salario_bruto*0.10
	print('> TOTAL DE DESCONTOS:\t\tR$ {:.2f}'.format(total_descontos))
	print('> SALÁRIO LÍQUIDO:\t\tR$ {:.2f}'.format(salario_bruto - total_descontos))

if __name__ == '__main__':
	main()