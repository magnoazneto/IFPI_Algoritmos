def main():
	turno = input('Selecione o turno que você estuda:\n\
M - Matutino\nV - Vespertino\nN - Noturno\n>>> ').upper()
	if turno == 'M':
		print('Bom dia!')
	elif turno == 'V':
		print('Boa tarde!')
	elif turno == 'N':
		print('Boa noite!')
	else:
		print('Por favor, verifique a entrada e tente novamente.')


if __name__ == '__main__':
	main()