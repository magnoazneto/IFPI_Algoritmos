import turtle

def main():
	bob = turtle.Turtle()
	lados = int((input('Defina um numero de lados: ')))
	tamanho = int(input('Defina o tamanho de um lado: '))
	square(bob, lados, tamanho)
	turtle.mainloop()


def square(t, lados, length):
	angulo = int(360 / lados)
	for i in range(lados):
		t.fd(length)
		t.lt(90)


if __name__ == '__main__':
	main()