def main():
	ENTRADA_1 = input().split(' ')
	ENTRADA_2 = input().split(' ')
	COD_1 = int(ENTRADA_1[0])
	NUM_1 = int(ENTRADA_1[1])
	VALOR_1 = float(ENTRADA_1[2])
	COD_2 = int(ENTRADA_2[0])
	NUM_2 = int(ENTRADA_2[1])
	VALOR_2 = float(ENTRADA_2[2])
	TOTAL = (NUM_1*VALOR_1) + (NUM_2*VALOR_2)
	print('VALOR A PAGAR: R$ {:.2f}'.format(TOTAL)) 


main()