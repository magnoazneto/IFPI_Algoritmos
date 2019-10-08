import turtle

def main():
	bob = turtle.Turtle()
	print(bob)
	square(bob, 100)
	turtle.mainloop()


def square(t, lado):
	for i in range(4):
		t.fd(100)
		t.lt(90)



if __name__ == '__main__':
	main()