from datetime import datetime
def main():
	nascimento = input('Digite a data do seu nascimento no formato DD/MM/AAAA: ').split('/')
	calcula_idade(nascimento)


def calcula_idade(nascimento):
	dia_nascimento = int(nascimento[0])
	mes_nascimento = int(nascimento[1])
	ano_nascimento = int(nascimento[2])
	now = datetime.now()
	atual = now.day + (now.month * 30) + (now.year*365)
	nascimento = dia_nascimento + (mes_nascimento*30) + (ano_nascimento*365)
	idade = atual - nascimento
	idade_anos = idade // 365
	idade_meses = (idade - (idade_anos*365)) // 30
	idade_dias = idade - (idade_anos*365) - (idade_meses*30)
	print('Você tem {} ano(s) {} mes(es) e {} dia(s)'.format(idade_anos, idade_meses, idade_dias)) 


if __name__ == '__main__':
	main()