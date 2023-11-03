from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title='Make your bets!',prompt='Which turtle will win the race? Enter a color: ')
colors = ['red','orange','yellow','green','blue','purple']
y_positions = [-125,-75,-25,25,75,125]

'''
pos1 = -200, -125
pos2 = -200, -75
pos3 = -200, -25
pos4 = -200,  25
pos5 = -200,  75
pos6 = -200,  125

turtle1 = Turtle(shape='turtle')
turtle1.color(colors[0])
turtle1.penup()
turtle1.goto(pos1)

turtle2 = Turtle(shape='turtle')
turtle2.color(colors[1])
turtle2.penup()
turtle2.goto(pos2)

turtle3 = Turtle(shape='turtle')
turtle3.color(colors[2])
turtle3.penup()
turtle3.goto(pos3)

turtle4 = Turtle(shape='turtle')
turtle4.color(colors[3])
turtle4.penup()
turtle4.goto(pos4)

turtle5 = Turtle(shape='turtle')
turtle5.color(colors[4])
turtle5.penup()
turtle5.goto(pos5)

turtle6 = Turtle(shape='turtle')
turtle6.color(colors[5])
turtle6.penup()
turtle6.goto(pos6)
'''
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -200, y = y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You\'ve won! The {winning_color} turtle is the winner!')
            else:
                print(f'You\'ve lost! The {winning_color} turtle is the winner')
                
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
    


screen.exitonclick()