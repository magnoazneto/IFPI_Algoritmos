def main():
	nota1 = float(input('Digite a primeira nota: '))
	nota2 = float(input('Digite a segunda nota: '))
	media = (nota1+nota2) / 2
	if media >= 7:
		print('Aprovado!')
	else:
		exame = float(input('Qual a nota do exame final? '))
		media = (media+exame) / 2
		if media >= 5:
			print('Aprovado!')
		else:
			print('Reprovado!')  


if __name__ == '__main__':
	main()