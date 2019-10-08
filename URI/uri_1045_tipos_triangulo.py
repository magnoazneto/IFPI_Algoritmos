def main():
	ABC = input().split()
	for c in range(0, 3):
		ABC[c] = float(ABC[c])
	ABC.sort(reverse = True)
	A, B, C = map(float, ABC)
	if A >= B + C:
		print('NAO FORMA TRIANGULO')
	elif (A**2) == (B**2) + (C**2):
		print('TRIANGULO RETANGULO')
	elif (A**2) > (B**2) + (C**2):
		print('TRIANGULO OBTUSANGULO')
	elif (A**2) < (B**2) + (C**2):
		print('TRIANGULO ACUTANGULO')
	if A == B == C:
		print('TRIANGULO EQUILATERO')
	elif A == B or B == C or A == C:
		print('TRIANGULO ISOSCELES')


main()