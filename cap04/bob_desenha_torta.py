import turtle
from modulos_bob import torta

def main():
	bob = turtle.Turtle()
	lados = int(input('Quantos lados terá o polígono? '))
	lateral = int(input('Qual o tamanho do raio? '))
	bob.color('black', 'red')
	giro_inicial = ((360/lados) / 2)
	bob.speed(7)
	bob.left(giro_inicial)
	torta(bob, lados, lateral)
	turtle.mainloop()

if __name__ == '__main__':
	main()