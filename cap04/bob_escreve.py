from letters import filtro, bob_config
import turtle

def main():
	bob = turtle.Turtle()
	palavra = input('Digite uma palavra para bob desenhar: ')
	bob_config(bob)
	filtro(bob, palavra)
	turtle.mainloop()


if __name__ == '__main__':
	main()