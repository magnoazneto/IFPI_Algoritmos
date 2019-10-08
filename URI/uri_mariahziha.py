def main():
	testes = int(input())
	for c in range(0, testes):
		valor = int(input())
		primo_check = primo(valor)
		if primo_check == True: 
			print('Prime')
		else:
			print('Not prime')

def primo(valor):  # checa se um valor é primo ou não
	total = 0
	for count in range(1, valor+1):
		if valor % count == 0:
			total += 1
	if total == 2:
		estado_primo = True
	else:
		estado_primo = False
	return estado_primo

main()