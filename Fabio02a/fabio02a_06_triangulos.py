def main():
	angulo1 = int(input('Digite o primeiro ângulo: '))
	angulo2 = int(input('Digite o segundo ângulo: '))
	angulo3 = int(input('Digite o terceiro ângulo: '))
	print(testa_triangulo(angulo1, angulo2, angulo3))


def testa_triangulo(angulo1, angulo2, angulo3):
	if angulo1 + angulo2 + angulo3 != 180 or angulo1 == 0 \
						  or angulo2 == 0 or angulo3 == 0:
		return 'Esses ângulos não formam um triângulo.'
	else:
		if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
			return 'Triângulo acutângulo!'
		elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
			return 'Triângulo retângulo!'
		elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
			return 'Triângulo obtusângulo!'


if __name__ == '__main__':
	main()