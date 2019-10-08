from math import sqrt
def main():
	x1 = float(input('Digite X1: '))
	y1 = float(input('Digite Y1: '))
	x2 = float(input('Digite X2: '))
	y2 = float(input('Digite Y2: '))
	calcula_area(x1, y1, x2, y2)


def calcula_area(x1, y1, x2, y2):
	largura = x1 - x2
	if largura < 0:
		largura = x2 - x1
	altura = y1 - y2
	if altura < 0:
		altura = y2 - y1
	print('Área do retângulo: {}'.format(altura*largura))


if __name__ == '__main__':
	main()