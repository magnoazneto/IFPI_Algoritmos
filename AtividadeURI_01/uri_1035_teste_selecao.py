def main():
	entradas = input().split(' ')
	A = int(entradas[0])
	B = int(entradas[1])
	C = int(entradas[2])
	D = int(entradas[3])
	if B > C and D > A and (C+D) > (A+B) and C > 0 and D > 0 and A % 2 == 0:
		print('Valores aceitos')
	else:
		print('Valores nao aceitos')


main()