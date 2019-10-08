def main():
	letra = input('Digite uma letra: ').upper()
	vogais = ['A', 'E', 'I', 'O', 'U']
	if letra in vogais:
		print('A letra é uma vogal.')
	else:
		print('A letra é uma consoante.')


if __name__ == '__main__':
	main()