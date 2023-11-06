from turtle import Turtle, Screen

def draw_triangle(t):
    for i in range(3):
        t.fd(100)
        t.right(120)


def draw_square(t):
    for i in range(4):
        t.fd(100)
        t.right(90)


def draw_pentagon(t):
    for i in range(5):
        t.fd(100)
        t.right(360/5)


def draw_hexagon(t):
    for i in range(6):
        t.fd(100)
        t.right(360/6)


def draw_heptagon(t):
    for i in range(7):
        t.fd(100)
        t.right(360/7)


def draw_octagon(t):
    for i in range(8):
        t.fd(100)
        t.right(360/8)


def draw_nonagon(t):
    for i in range(9):
        t.fd(100)
        t.right(360/9)



def draw_decagon(t):
    for i in range(10):
        t.fd(100)
        t.right(360/10)



timmy = Turtle()
timmy.shape('turtle')
timmy.color('green')
draw_triangle(timmy)
draw_square(timmy)
draw_pentagon(timmy)
draw_hexagon(timmy)
draw_heptagon(timmy)
draw_octagon(timmy)
draw_nonagon(timmy)
draw_decagon(timmy)



screen = Screen()
screen.exitonclick()