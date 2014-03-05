def main():
	wn = turtle.Screen()  
	alex = turtle.Turtle() 
	alex.speed('fastest')
	for i in range(1000):
		if i % 2 == 0:
			alex.color('red')
		else:
			alex.color('blue')
		alex.forward(i)
		alex.left(262)
	turtle.mainloop()
main()