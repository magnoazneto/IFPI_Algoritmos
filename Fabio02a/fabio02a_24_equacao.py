from math import sqrt
def main():
	A = int(input('Coeficiente A: '))
	B = int(input('Coeficiente B: '))
	C = int(input('Coeficiente C: '))
	calcula_delta(A, B, C)


def calcula_delta(a, b, c):
	delta = (b**2) - (4*a*c)
	if delta < 0:
		print('Delta negativo. Não é possível calcular.')
	elif delta == 0:
		print('Apenas 1 raiz real.')
		raiz = (-b + sqrt(delta)) / (2*a)
		print('Raiz: {}'.format(raiz))
	else:
		raiz1 = (-b + sqrt(delta)) / (2*a)
		raiz2 = (-b - sqrt(delta)) / (2*a)
		print('Raiz 1: {}'.format(raiz1))
		print('Raiz 2: {}'.format(raiz2))
	

if __name__ == '__main__':
	main()