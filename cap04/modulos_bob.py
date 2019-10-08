import turtle
import math

# Funções para cálculos gerais

# CALCULA O CATETO OPOSTO DE TRIANGULO PARA CONSTRUÇÃO DE POLIGONO
# LADOS: Numero de lados que o poligono terá

def cateto_oposto(lados, hipotenusa):
	angulo = (360 / lados) / 2
	angulo = math.radians(angulo)
	seno = math.sin(angulo)
	cateto_oposto = round(seno * hipotenusa)
	return cateto_oposto

# Funções para movimentação geral do bob

def polygono(t, lados, length):  # POLÍGONO
	angulo = 360 / lados
	for i in range(lados):
		t.fd(length)
		t.lt(angulo)


def circle(t, raio):  # CIRCULO
	circunferencia = 2 * math.pi * raio
	#tamanho_polygono = int(circunferencia / 3)
	length = circunferencia / 50
	polygono(t, raio, length)


def circle_2(t, raio):  # VARIAÇÃO MAIS PRECISA NO DESENHO DE CÍRCULO
	arc(t, r, 360)


# Funções para movimentações mais elaboradas

def arc(t, raio, angle):  # ARCO
	tamanho_arco = (2 * math.pi * raio * angle) / 360
	tamanho_polygono = int(tamanho_arco / 3) + 1
	step_length = tamanho_arco / tamanho_polygono
	step_angle = float(angle) / tamanho_polygono 
	polyline(t, tamanho_polygono, step_length, step_angle)


def polyline(t, tamanho_polygono, length, angle):  # POLILINHA
	for c in range(tamanho_polygono):
		t.fd(length)
		t.lt(angle)


# Funções que usam outras funções em cadeia para construir desenhos


def petala(t, raio, angulo):  # DESENHAR PÉTALAS
	for i in range(2):
		arc(t, raio, angulo)
		t.lt(180 - angulo)


def flor(t, raio, angulo, petalas):  # DESENHAR UMA FLOR COMPLETA
	for c in range(petalas):
		petala(t, raio, angulo)
		t.lt(360 / petalas)


def triangulo(t, lados, lateral):  # DESENHAR TRIANGULO ISÓSCELES
	base = (cateto_oposto(lados, lateral)) * 2
	giro_inicial = ((360/lados) / 2)
	angulo_giro = 180 - (180 - (giro_inicial+90))
	t.forward(lateral)
	t.left(angulo_giro)
	t.forward(base)
	t.left(angulo_giro)
	t.forward(lateral)
	t.left(180)


def torta(t, lados, base):  # DESENHAR TORTA
	for c in range(lados):
		if c % 2 == 0: 
			t.begin_fill()
		triangulo(t, lados, base)
		if c % 2 == 0:
			t.end_fill()