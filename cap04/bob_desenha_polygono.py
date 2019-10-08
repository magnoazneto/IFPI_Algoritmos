import turtle
from modulos_bob import polygono

def main():
	bob = turtle.Turtle()
	lados = int((input('Defina um numero de lados do polígono: ')))
	tamanho = int(input('Defina o tamanho de um lado: '))
	polygono(bob, lados, tamanho)
	turtle.mainloop()


if __name__ == '__main__':
	main()