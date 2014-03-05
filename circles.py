import turtle
import random

# random pastel color generator
def randColor():
	r = str(hex(round(random.random() * 127 + 127 )))[2:]
	g = str(hex(round(random.random() * 127 + 127 )))[2:]
	b = str(hex(round(random.random() * 127 + 127 )))[2:]
	color = "#"+r+g+b
	return color

def main():

	wn = turtle.Screen()  
	alex = turtle.Turtle() 

	alex.speed('fastest')
	alex.pensize(3)

	alex.goto(0,0)
	for i in range(45):
		alex.color(randColor())
		alex.circle(100)
		alex.left(8)

	turtle.mainloop()

main()