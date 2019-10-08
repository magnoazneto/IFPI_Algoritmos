from math import sqrt
def main():
	numero = int(input('Digite um número de 4 digitos: '))
	checa_quadrado_perfeito(numero)

def checa_quadrado_perfeito(numero):
	parte1 = numero // 100
	parte2 = numero % 100
	if sqrt(numero) == parte1 + parte2:
		print('O número é um quadrado perfeito!')
		print('sqrt({}) = {} = {} + {}'.format(numero, sqrt(numero), parte1, parte2))
	else:
		print('Desculpe. Este não é um quadrado perfeito.')
		print('sqrt({}) = {:.2f} != {} + {}'.format(numero, sqrt(numero), parte1, parte2))


if __name__ == '__main__':
	main()