from turtle import *


shape("turtle")
pensize(15)

def movefd(x):
   pu()
   fd(x)
   pd()

def go(t,p):
   t.pu()
   t.goto(p)
   t.pd()
   t.setheading(0)

def space(x):
   pu()
   fd(1.5*x)
   pd()

def zero(x):
   for i in range(2):
       fd(x)
       rt(90)
       fd(2*x)
       rt(90)

def one(x):
   start = pos()
   movefd(x)
   rt(90)
   fd(2*x)
   pu()
   goto(start)
   pd()
   setheading

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
   goback(start)

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
   go(start)

def four(x):
   start = pos()
   movefd(x)
   rt(90)
   fd(2*x)
   go(start)
   rt(90)
   fd(x)
   lt(90)
   fd(x)
   start()

def five(x):
   start = pos()
   fd(x)
   for i in range(3):
       bk(x)
       lt(90)
   fd(x)
   rt(90)
   fd(x)
   go(start)


def six(x):
   start = pos()
   rt(90)
   fd(2*x)
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
   rt(90)
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


def check(i,x):
   if (i == 0):
       zero(x)
   elif(i == 1):
       one(x)
   elif(i == 2):
       two(x)
   elif(i == 3):
       three(x)
   elif(i == 4):
       four(x)
   elif(i == 5):
       five(x)
   elif(i == 6):
       six(x)
   elif(i == 7):
       seven(x)
   elif(i == 8):
       eight(x)
   elif(i == 9):
       nine(x)




exitonclick()