def main():
	num1, num2 = map(int, input().split())
	somador(num1, num2)


def somador(num1, num2):
	num1_bin = dec2bin(num1)
	num2_bin = dec2bin(num2)
	printa_binario(num1_bin)
	printa_binario(num2_bin)


def dec2bin(numero):
	numero = str(bin(numero))
	binario = []
	for e in numero:
		if e == 'b':
			binario.append('0')
		else:
			binario.append(e)

	for c in range(0, 32):
		if binario[c]:
			if binario[c] not in range(0, 2):
				binario.insert(0, '0')
		else:
			binario.insert(0, '0')
	return binario


def printa_binario(numero):
	for c in numero:
		print(c, end='')
	print()



main()
