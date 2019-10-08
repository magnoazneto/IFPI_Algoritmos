import turtle

def main():
	bob = turtle.Turtle()
	bob.pensize(1)
	bob.speed(1)
	draw(bob, 50, 4)
	turtle.mainloop()


def draw(t, length, n):
	if n == 0:
		return
	angle = 50
	t.fd(length * n)
	t.lt(angle)
	draw(t, length, n-1)
	t.rt(2 * angle)
	draw(t, length, n-1)
	t.lt(angle)
	t.bk(length * n)


if __name__ == '__main__':
	main()