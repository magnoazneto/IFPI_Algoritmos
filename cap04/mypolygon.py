import turtle
import math

def polygon(t, n, lenght):
	angulo = int(360 / n)
	for c in range(n):
		t.fd(lenght)
		t.lt(angulo)


def circle(t, r, tamanho_polygono):
	circunferencia = 2 * math.pi * r
	lenght = circunferencia / tamanho_polygono
	polygon(t, tamanho_polygono, lenght)


bob = turtle.Turtle()
print(bob)
tamanho = int(input('Digite o tamanho: '))
lados = int(input('Digite o numero de lados: '))
raio = int(input('Digite o raio: '))
polygon(bob, lados, tamanho)
circle(bob, raio, tamanho)


turtle.mainloop()
