import turtle
from modulos_bob import flor


def main():
	bob = turtle.Turtle()
	opcao(bob)
	turtle.mainloop()


def opcao(t):
	option = int(input('Selecione 1 opção:\n\
1 - Para liberdade total nas proporções da flor\n\
2 - Para que o programa deixe-a sem pétalas cruzadas:\n> '))
	if option == 1:
		angulo = int(input('Desenhe o ângulo da pétala: '))
		raio = int(input('Digite o raio da pétala: '))
		petalas = int(input('Digite o numero de pétalas que sua flor terá: '))
		flor(t, raio, angulo, petalas)
	elif option == 2:
		petalas = int(input('Quantas pétalas você quer que sua flor tenha? '))
		raio = int(input('Digite o raio das pétalas, pois isso influenciará \
no tamanho de visualização da flor: '))
		angulo = 360 / petalas
		flor(t, raio, angulo, petalas)


if __name__ == '__main__':
	main()
