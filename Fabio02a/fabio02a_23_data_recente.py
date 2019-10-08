def main():
	data1 = input('Digite a data 1 no formato DIA/MES/ANO: ').split('/')
	data2 = input('Digite a data 2 no formato DIA/MES/ANO: ').split('/')
	calcula_data(data1, data2)


def calcula_data(data1, data2):
	dia1 = int(data1[0])
	mes1 = int(data1[1])
	ano1 = int(data1[2])
	dia2 = int(data2[0])
	mes2 = int(data2[1])
	ano2 = int(data2[2])
	if dia1 > 31 or dia2 > 31 or mes1 > 12 or mes2 > 12:
		print('Data inválida.')
		main()
	primeira_data = (ano1*365) + (mes1*30) + dia1
	segunda_data = (ano2*365) + (mes2*30) + dia2
	if primeira_data > segunda_data:
		print('A data {}/{}/{} é mais recente.'.format(dia1, mes1, ano1))
	elif primeira_data == segunda_data:
		print('As datas são iguais.')
	else:
		print('A data {}/{}/{} é mais recente'.format(dia2, mes2, ano2))


if __name__ == '__main__':
	main()