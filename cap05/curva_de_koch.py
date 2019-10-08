import turtle
from modulos_bob import demo_koch, snowflake

def main():
	squirtle = turtle.Turtle()
	squirtle.penup()
	squirtle.setposition(-200, 100)
	squirtle.pendown()
	opcao(squirtle)
	turtle.mainloop()


def opcao(t):
	opcao = int(input('Selecione uma opção:\n\
1 - Desenhar 3 linhas de koch para demonstração.\n\
2 - Desenhar um fractai de gelo.'))
	if opcao == 1:
		t.speed(10)
		demo_koch(t, 100)
	elif opcao == 2:
		comprimento = int(input('Digite o comprimento da curva de Koch: '))
		speed = int(input('Digite a velocidade de desenho do bob: '))
		if comprimento > 0:
			t.speed(speed)
			snowflake(t, comprimento)
		else:
			print('Por favor, digite um comprimento maior que 0.')
			opcao()
	else:
		print('Por favor, digite uma opção válida.')
		opcao()


if __name__ == '__main__':
	main()