def main():
	x, y = map(float, input().split())
	print(filtro_quadrante(x, y))

def filtro_quadrante(x, y):
	if x == y == 0: return 'Origem'
	elif x == 0 or y == 0: return 'Eixo Y' if x == 0 else 'Eixo X'
	elif x > 0:
		return 'Q1' if y > 0 else 'Q4'
	elif x < 0:
		return 'Q2' if y > 0 else 'Q3'


main()