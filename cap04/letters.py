import turtle

def filtro(t, palavra):
	palavra = palavra.lower()
	tamanho = len(palavra)
	letras = []
	count = 0
	eixo_y = 200
	for c in range(tamanho):
		letras.append(palavra[c])
	for c in range(tamanho):
		t.pendown()
		if letras[c] == 'a':
			draw_a(t)
		elif letras[c] == 'b':
			draw_b(t)
		elif letras[c] == 'c':
			draw_c(t)
		elif letras[c] == 'd':
			draw_d(t)
		elif letras[c] == 'e':
			draw_e(t)
		elif letras[c] == 'f':
			draw_f(t)
		elif letras[c] == 'g':
			draw_g(t)
		elif letras[c] == 'h':
			draw_h(t)
		elif letras[c] == 'i':
			draw_i(t)
		elif letras[c] == 'j':
			draw_j(t)
		elif letras[c] == 'k':
			draw_k(t)
		elif letras[c] == 'l':
			draw_l(t)
		elif letras[c] == 'm':
			draw_m(t)
		elif letras[c] == 'n':
			draw_n(t)
		elif letras[c] == 'o':
			draw_o(t)
		elif letras[c] == 'p':
			draw_p(t)
		elif letras[c] == 'q':
			draw_q(t)
		elif letras[c] == 'r':
			draw_r(t)
		elif letras[c] == 's':
			draw_s(t)
		elif letras[c] == 't':
			draw_t(t)
		elif letras[c] == 'u':
			draw_u(t)
		elif letras[c] == 'v':
			draw_v(t)
		elif letras[c] == 'w':
			draw_w(t)
		elif letras[c] == 'x':
			draw_x(t)
		elif letras[c] == 'y':
			draw_y(t)
		elif letras[c] == 'z':
			draw_z(t)
		elif letras[c] == ' ':
			draw_space(t)
		t.penup()
		count += 1
		if count >= 18:
			eixo_y -= 60
			t.setposition(-300, eixo_y )
			count = 0
		else:
			t.fd(10)


def bob_config(t):
	t.speed(30)
	t.pensize(2)
	t.penup()
	t.setposition(-300, 200)
	t.pendown()

def bob_step_left(t, angle, step):
	t.left(angle)
	t.fd(step)

def bob_step_right(t, angle, step):
	t.right(angle)
	t.fd(step)

def bob_go_and_back(t):
	t.right(90)
	t.fd(26)
	t.right(180)
	t.fd(26)


def draw_space(t):
	t.penup()
	t.fd(10)
	t.pendown()


def draw_a(t):
	bob_step_left(t, 90, 50)
	bob_step_right(t, 90, 26)
	bob_step_right(t, 90, 25)
	bob_go_and_back(t)
	bob_step_right(t, 90, 25)
	t.left(90)


def draw_b(t):
	bob_step_left(t, 90, 50)
	bob_step_right(t, 90, 26)
	bob_step_right(t, 90, 25)
	bob_go_and_back(t)
	bob_step_right(t, 90, 25)
	bob_go_and_back(t)


def draw_c(t):
	bob_step_left(t, 90, 50)
	bob_step_right(t, 90, 26)
	t.penup()
	bob_step_right(t, 90, 50)
	t.pendown()
	bob_go_and_back(t)


def draw_d(t):
	bob_step_left(t, 90, 50)
	bob_step_right(t, 90, 20)
	bob_step_right(t, 45, 11)
	bob_step_right(t, 45, 35)
	bob_step_right(t, 45, 11)
	bob_step_right(t, 45, 20)
	bob_step_right(t, 180, 20)
	t.penup()
	t.fd(6)


def draw_e(t):
	bob_step_left(t, 90, 50)
	bob_go_and_back(t)
	bob_step_left(t, 90, 25)
	t.left(180)
	bob_go_and_back(t)
	bob_step_left(t, 90, 25)
	bob_step_left(t, 90, 26)


def draw_f(t):
	bob_step_left(t, 90, 50)
	bob_go_and_back(t)
	bob_step_left(t, 90, 25)
	t.right(180)
	bob_go_and_back(t)
	bob_step_left(t, 90, 25)
	t.penup()
	bob_step_left(t, 90, 26)


def draw_g(t):
	bob_step_left(t, 90, 50)
	bob_go_and_back(t)
	bob_step_left(t, 90, 50)
	bob_step_left(t, 90, 26)
	bob_step_left(t, 90, 25)
	bob_step_left(t, 90, 13)
	bob_step_left(t, 180, 13)
	bob_step_right(t, 90, 25)
	t.left(90)


def draw_h(t):
	bob_step_left(t, 90, 50)
	bob_step_left(t, 180, 25)
	bob_step_left(t, 90, 26)
	bob_step_left(t, 90, 25)
	bob_step_left(t, 180, 50)
	t.left(90)


def draw_i(t):
	bob_step_left(t, 90, 50)
	bob_step_left(t, 180, 50)
	t.left(90)


def draw_j(t):
	t.fd(26)
	bob_step_left(t, 90, 50)
	bob_step_left(t, 180, 50)
	t.left(90)


def draw_k(t):
	bob_step_left(t, 90, 50)
	bob_step_left(t, 180, 25)
	bob_step_left(t, 135, 35)
	bob_step_left(t, 180, 35)
	bob_step_left(t, 90, 35)
	t.left(45)


def draw_l(t):
	bob_step_left(t, 90, 50)
	bob_step_left(t, 180, 50)
	bob_step_left(t, 90, 26)


def draw_m(t):
	bob_step_left(t, 90, 50)
	bob_step_right(t, 135, 30)
	bob_step_left(t, 90, 30)
	bob_step_right(t, 135, 50)
	t.left(90)


def draw_n(t):
	bob_step_left(t, 90, 50)
	bob_step_right(t, 145, 60)
	bob_step_left(t, 145, 50)
	bob_step_right(t, 180, 50)
	t.left(90)


def draw_o(t):
	bob_step_left(t, 90, 50)
	bob_go_and_back(t)
	bob_step_left(t, 90, 50)
	bob_step_left(t, 90, 26)
	bob_step_left(t, 90, 50)
	bob_step_left(t, 180, 50)
	t.left(90)


def draw_p(t):
	bob_step_left(t, 90, 50)
	bob_step_right(t, 90, 26)
	bob_step_right(t, 90, 25)
	bob_step_right(t, 90, 26)
	bob_step_left(t, 90, 25)
	t.penup()
	bob_step_left(t, 90, 26)


def draw_q(t):
	bob_step_left(t, 90, 50)
	bob_step_right(t, 90, 26)
	bob_step_right(t, 90, 50)
	bob_step_right(t, 90, 26)
	bob_step_right(t, 180, 26)
	bob_step_left(t, 135, 10)
	bob_step_left(t, 180, 20)
	bob_step_left(t, 180, 10)
	t.right(135)


def draw_r(t):
	bob_step_left(t, 90, 50)
	bob_step_right(t, 90, 26)
	bob_step_right(t, 90, 25)
	bob_step_right(t, 90, 26)
	bob_step_left(t, 135, 36)
	t.left(45)


def draw_s(t):
	t.fd(26)
	bob_step_left(t, 90, 25)
	bob_step_left(t, 90, 26)
	bob_step_right(t, 90, 25)
	bob_step_right(t, 90, 26)
	t.penup()
	bob_step_right(t, 90, 50)
	t.left(90)


def draw_t(t):
	t.penup()
	t.fd(13)
	t.pendown()
	bob_step_left(t, 90, 50)
	bob_step_left(t, 90, 13)
	bob_step_right(t, 180, 26)
	t.penup()
	bob_step_right(t, 90, 50)
	t.left(90)


def draw_u(t):
	bob_step_left(t, 90, 50)
	bob_step_left(t, 180, 50)
	bob_step_left(t, 90, 26)
	bob_step_left(t, 90, 50)
	bob_step_left(t, 180, 50)
	t.left(90)


def draw_v(t):
	t.penup()
	t.fd(13)
	t.pendown()
	bob_step_left(t, 70, 52)
	bob_step_left(t, 180, 52)
	bob_step_right(t, 140, 52)
	bob_step_right(t, 180, 52)
	t.penup()
	bob_step_left(t, 70, 13)


def draw_w(t):
	bob_step_left(t, 90, 50)
	bob_step_right(t, 180, 50)
	bob_step_left(t, 135, 30)
	bob_step_right(t, 90, 30)
	bob_step_left(t, 135, 50)
	bob_step_left(t, 180, 50)
	t.left(90)


def draw_x(t):
	bob_step_left(t, 60, 56)
	bob_step_left(t, 180, 28)
	bob_step_right(t, 120, 28)
	bob_step_right(t, 180, 56)
	t.left(60)


def draw_y(t):
	t.penup()
	t.fd(13)
	t.pendown()
	bob_step_left(t, 90, 25)
	bob_step_left(t, 45, 28)
	bob_step_right(t, 180, 28)
	bob_step_left(t, 90, 28)
	bob_step_right(t, 180, 28)
	bob_step_left(t, 45, 25)
	t.penup()
	bob_step_left(t, 90, 14)


def draw_z(t):
	t.penup()
	bob_step_left(t, 90, 50)
	t.pendown()
	bob_step_right(t, 90, 26)
	bob_step_right(t, 120, 56)
	bob_step_left(t, 120, 26)
