def main():
	lado1 = float(input('Digite o primeiro lado do triângulo: '))
	lado2 = float(input('Agora, o segundo lado: '))
	lado3 = float(input('Terceiro lado: '))
	triangulo(lado1, lado2, lado3)


def triangulo(medida1, medida2, medida3):
	if medida1 >= medida2 + medida3 or medida2 >= medida1 + medida3 or medida3 >= medida1 + medida2:
		if medida1 == medida2 + medida3 or medida2 == medida1 + medida3 or medida3 == medida1 + medida2:
			print('Triângulo degenerado!')
		else:
			print('Não é possível formar um triângulo com essas medidas.')
	else:
		print('É possível formar um triângulo com essas medidas!')
		if medida1 == medida2 or medida1 == medida3 or medida2 == medida3:
			if medida1 == medida2 == medida3:
				print('Esse já é um triângulo equilátero. Seus lados são todos iguais.')
			else:
				print('Ele será isosceles!')
		else:
			print('Ele será escaleno!')
			if (medida1**2) == ((medida2**2) + (medida3**2)):
				print('O lado {} corresponde a Hipotenusa, e os lados \
{} e {} aos catetos.'.format(medida1, medida2, medida3))
			elif (medida2**2) == ((medida1**2) + (medida3**2)):
				print('O lado {} corresponde a Hipotenusa, e os lados \
{} e {} aos catetos.'.format(medida2, medida1, medida3))
			elif (medida3**2) == ((medida2**2) + (medida1**2)):
				print('O lado {} corresponde a Hipotenusa, e os lados \
{} e {} aos catetos.'.format(medida3, medida2, medida1))
			else:
				print('No entanto, não será um triângulo retângulo.')


if __name__ == '__main__':
	main()