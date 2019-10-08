def main():
	ENTRADA = int(input())
	ANOS = ENTRADA // 365
	MESES = (ENTRADA - (ANOS*365)) // 30
	DIAS = ENTRADA - (ANOS*365) - (MESES*30)
	print('{} ano(s)'.format(ANOS))
	print('{} mes(es)'.format(MESES))
	print('{} dia(s)'.format(DIAS))


main()