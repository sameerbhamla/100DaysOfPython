import turtle
from turtle import *


def go(p):
    pu()
    goto(p)
    pd()
    setheading(0)


def go(t, p):
    t.pu()
    t.goto(p)
    t.pd()
    t.setheading(0)


def movefd(t: turtle, x: int):
    t.pu()
    t.fd(x)
    t.pd()


def zero():
    for i in range(360):
        myTurtle.fd(1)
        myTurtle.rt(1)


def one(t):
    t.hideturtle()
    start = pos()
    t.rt(135)
    t.fd(100)
    t.goto(start)
    t.lt(45)
    t.fd(200)
    t.lt(90)
    t.fd(80)
    t.lt(180)
    t.fd(160)


def two(x):
    start = pos()
    fd(x)
    rt(90)
    fd(x)
    rt(90)
    fd(x)
    lt(90)
    fd(x)
    lt(90)
    fd(x)


def three(x):
    fd(x)
    rt(90)
    fd(x)
    rt(90)
    fd(x)
    bk(x)
    lt(90)
    fd(x)
    rt(90)
    fd(x)


def four(t, x):
    start = t.pos()
    movefd(t, x)
    t.rt(90)
    t.fd(2 * x)
    go(t, start)
    t.rt(90)
    t.fd(x)
    t.lt(90)
    t.fd(x)


def five(t, x):
    start = t.pos()
    t.fd(x)
    for i in range(3):
        t.bk(x)
        t.lt(90)
    t.fd(x)
    t.rt(90)
    t.fd(x)
    t.penup()
    t.goto(start)


def six(x):
    start = pos()
    rt(90)
    fd(2 * x)
    lt(90)
    fd(x)
    lt(90)
    fd(x)
    lt(90)
    fd(x)
    go(start)
    fd(x)
    go(start)

def seven(x):
   start = pos()
   fd(x)
   rt(110)
   fd(2*x)
   go(start)


def eight(x):
   start = pos()
   for i in range(4):
       fd(x)
       rt(90)
   for i in range(2):
       fd(x)
       rt(90)
       fd(2*x)
       rt(90)


def nine(x):
   start = pos()

   fd(x)
   rt(90)
   fd(2*x)
   bk(x)
   rt(90)
   fd(x)
   rt(90)
   fd(x)
   go(start)


window = turtle.Screen()
# window.tracer(0)
myTurtle = turtle.Turtle()

myTurtle.shape('turtle')
myTurtle.speed(1)
four(myTurtle,100)

window.update()
window.mainloop()
exitonclick()
