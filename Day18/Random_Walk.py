from turtle import Turtle,Screen
import random
def pick_random():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color



screen = Screen()
screen.colormode(255)
colors = ['red','blue','green','orange','yellow','purple']
directions = [0,90,180,270]
timmy = Turtle()
timmy.color(random.choice(colors))
timmy.pensize(15)
timmy.speed(8)
running = True

while(running):
    timmy.fd(30)
    timmy.right(random.choice(directions))
    timmy.color(pick_random())

screen.exitonclick()