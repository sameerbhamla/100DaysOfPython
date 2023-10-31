from turtle import Turtle, Screen
import random

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color


screen = Screen()
screen.colormode(255)

tim = Turtle()
tim.speed("fastest")

for i in range(1000):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading()+10)


screen.exitonclick()