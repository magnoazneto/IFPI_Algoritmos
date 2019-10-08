def main():
	nota1 = float(input('Digite a primeira nota: '))
	nota2 = float(input('Digite a segunda nota: '))
	conceito = conceito_nota((nota1+nota2) / 2)
	boletim(nota1, nota2, conceito)


def conceito_nota(media):
	if media < 0 or media > 10:
		conceito = 'Notas Inválidas'
	elif media >= 9.0:
		conceito = 'A'
	elif media >= 7.5:
		conceito = 'B'
	elif media >= 6.0:
		conceito = 'C'
	elif media >= 4.0:
		conceito = 'D'
	else:
		conceito = 'E'
	return conceito


def boletim(nota1, nota2, conceito):
	media = (nota1+nota2) / 2
	if conceito in ['A', 'B', 'C']:
		situacao = 'APROVADO'
	else:
		situacao = 'REPROVADO'

	print('=========BOLETIM SEMESTRAL==============')
	print('NOTA 1:\t\t\t{}'.format(nota1))
	print('NOTA 2:\t\t\t{}'.format(nota2))
	print('MEDIA:\t\t\t{}'.format(media))
	print('CONCEITO:\t\t{}'.format(conceito))
	print('SITUAÇÃO:\t\t{}'.format(situacao))


if __name__ == '__main__':
	main()