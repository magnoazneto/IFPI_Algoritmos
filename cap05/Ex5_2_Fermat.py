def main():
	a = int(input("Digite o valor de a: "))
	b = int(input("Digite o valor de b: "))
	c = int(input("Digite o valor de c: "))
	n = int(input("Digite o valor de n: "))
	check_fermat(a, b, c, n)


def check_fermat(a, b, c, n):
	if n > 2 and (a**n) + (b**n) == (c**n):
		print('Holy smokes, Fermat was wrong!')
	elif n <= 2:
		print("That doesn't work and you have to enter > 2 values.")
	else:
		print("No, that doesn't work.")


if __name__ == '__main__':
	main()