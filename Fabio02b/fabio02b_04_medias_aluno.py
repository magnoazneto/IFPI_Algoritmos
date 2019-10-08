def main():
	nota1 = float(input('Digite a primeira nota: '))
	nota2 = float(input('Digite a segunda nota: '))
	media = (nota1+nota2) / 2
	if media < 7:
		print('Reprovado.')
	elif media < 10:
		print('Aprovado.')
	else:
		print('Aprovado com distinção.')


if __name__ == '__main__':
	main()