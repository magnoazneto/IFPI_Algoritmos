def main():
	entradas = input().split()
	A = float(entradas[0])
	B = float(entradas[1])
	C = float(entradas[2])
	tria_retangulo = (A*C) / 2
	circulo = 3.14159 * (C**2)
	trapezio = ((A+B) * C) / 2
	quadrado = B ** 2
	retangulo = A * B
	print('TRIANGULO: {:.3f}'.format(tria_retangulo))
	print('CIRCULO: {:.3f}'.format(circulo))
	print('TRAPEZIO: {:.3f}'.format(trapezio))
	print('QUADRADO: {:.3f}'.format(quadrado))
	print('RETANGULO: {:.3f}'.format(retangulo))


main()