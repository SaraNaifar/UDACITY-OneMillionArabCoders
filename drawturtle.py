import turtle
import random

def draw_square(animal):

	animal.forward(5)

	animal.circle(50)
	animal.forward(3)
	
	
def draw_turtle():
	r = lambda: random.randint(0,255)
	window= turtle.Screen()
	window.colormode(255)
	
	window.bgcolor("white")
	ninja= turtle.Turtle()
	ninja.shape("turtle")
	ninja.speed(100)
	for k in range(5):

		
		ninja.color(r(),r(),r())
		for i in range(36):
			draw_square(ninja)
			ninja.right(12)
		ninja.forward(50)
	window.exitonclick()

draw_turtle()

