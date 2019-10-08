def main():
	dia, mes, ano = map(int, input('Digite a data: ').split('/'))
	print('Data válida.') if testa_data(dia, mes, ano) else print('Data inválida.')


def testa_data(dia, mes, ano):
	if dia > 31 or dia <=0 or mes > 12 or mes < 0 or ano <= 0:
		return False
	elif (mes % 2 == 0 and mes < 8) or (mes % 2 != 0 and mes >= 8): # Checa regra dos dedos
		if (mes == 2 and dia > 29) or (dia > 30):
			return False
		else:
			if mes == 2 and dia == 29:
				return True if ano_bisexto(ano) else False
			else:
				return True
	else:
		return True


def ano_bisexto(ano):
	if ano % 4 == 0 

if __name__ == '__main__':
	main()