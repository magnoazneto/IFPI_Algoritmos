def main():
	a, b = map(int, input().split())
	print(multiplos(a, b))


def multiplos(a, b):
	return 'Sao Multiplos' if a % b == 0 or b % a == 0 else 'Nao sao Multiplos'


main()