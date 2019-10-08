import turtle
from modulos_bob import circle

def main():
	bob = turtle.Turtle()
	raio = int(input('Qual o raio do circulo? '))
	circle(bob, raio)
	turtle.mainloop()


if __name__ == '__main__':
	main()