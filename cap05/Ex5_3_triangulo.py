def main():
	medida1 = int(input('Digite a primeira medida do triângulo: '))
	medida2 = int(input('Digite a segunda medida do triângulo: '))
	medida3 = int(input('Digite a terceira medida do triângulo: '))
	is_triangle(medida1, medida2, medida3)


def is_triangle(medida1, medida2, medida3):
	if medida1 >= medida2 + medida3 or medida2 >= medida1 + medida3 or medida3 >= medida1 + medida2:
		if medida1 == medida2 + medida3 or medida2 == medida1 + medida3 or medida3 == medida1 + medida2:
			print('Triângulo degenerado!')
		else:
			print('Não é possível formar um triângulo com essas medidas.')
	else:
		print('É possível formar um triângulo com essas medidas!')
		if medida1 == medida2 or medida1 == medida3 or medida2 == medida3:
			if medida1 == medida2 == medida3:
				print('Ele será equilatero!')
			else:
				print('Ele será isosceles!')
		else:
			print('Ele será escaleno!')


if __name__ == '__main__':
	main()