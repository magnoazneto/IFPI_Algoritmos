import turtle
from modulos_bob import arc

def main():
	bob = turtle.Turtle()
	raio = int(input('Qual o raio do arco? '))
	angulo = int(input('Digite o angulo: '))
	arc(bob, raio, angulo)
	turtle.mainloop()


if __name__ == '__main__':
	main()