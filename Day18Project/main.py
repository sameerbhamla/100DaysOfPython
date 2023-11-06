"""
import colorgram

rgb_colors = []
colors = colorgram.extract('HirstPainting.jpg',30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.g
    new_color = (r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)
"""

from turtle import Turtle, Screen, colormode
import random


color_list = [(132, 166, 166), (221, 148, 148), (32, 42, 42), (199, 135, 135), (166, 58, 58), (141, 184, 184), (39, 105, 105), (237, 212, 212), (150, 59, 59),
              (216, 82, 82),(168, 29, 29), (235, 165, 165), (51, 111, 111), (35, 61, 61), (156, 33, 33), (17, 97, 97), (52, 44, 44), (230, 161, 161), (170, 188, 188),
              (57, 51, 51), (184, 103, 103), (32, 60, 60), (105, 126, 126), (175, 200, 200), (34, 151, 151), (65, 66, 66)]

timmy = Turtle()
colormode(255)
timmy.speed('fastest')
timmy.penup()
reset_x = -430

start_x = -430
start_y = 360

for i in range(10):
    for j in range(10):
        timmy.setpos(start_x, start_y)
        timmy.dot(60, random.choice(color_list))
        start_x += 95
    start_x = reset_x
    start_y -= 90


screen = Screen()
screen.exitonclick()