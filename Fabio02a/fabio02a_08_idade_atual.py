def main():
	dia_atual = int(input('Digite o dia de hoje: '))
	mes_atual = int(input('Digite o mês atual: '))
	ano_atual = int(input('Digite o ano atual: '))
	dia_nascimento = int(input('Digite o dia do seu nascimento: '))
	mes_nascimento = int(input('Digite o mês do seu nascimento: '))
	ano_nascimento = int(input('Digite a ano nascimento: '))
	print('Hoje, você tem {} anos.'.format(calcula_idade(dia_atual,\
mes_atual, ano_atual, dia_nascimento, mes_nascimento, ano_nascimento)))


def calcula_idade(dia_atual, mes_atual, ano_atual, dia_nascimento,\
mes_nascimento, ano_nascimento):
	ano = ano_atual - ano_nascimento
	if mes_atual <= mes_nascimento:
		if dia_atual < dia_nascimento:
			ano = ano - 1
	return ano


if __name__ == '__main__':
	main()
