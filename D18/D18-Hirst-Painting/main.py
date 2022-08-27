# import colorgram

# Code below generates a list of tuples whose output is hard coded as "color_list"
# rgb_colors = []
# colors = colorgram.extract('./hirst-dots-image.jpg', 12)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle
from turtle import Turtle, Screen
import random

def random_color():
    return random.choice(color_list)


turtle.colormode(255)
color_list = [(132, 164, 203), (227, 149, 99), (30, 43, 64), (166, 58, 47), (202, 135, 148), (237, 212, 86),
              (41, 102, 150), (135, 182, 161)]

# Project Specs
# paint 10 x 10 grid of dots
# dots to be 20 units in diameter
# dot to be spaced 50 units apart

joe = Turtle()
joe.shape("turtle")
joe.color("dark green")
joe.speed("fastest")

# Set tutle to new location
joe.penup()
joe.goto(-250, -250)
x = -250
y = -250

total_dots = 100

# Generate 100 dots
for dot_count in range(1, total_dots + 1):
    joe.pendown()
    joe.dot(20, random_color())
    joe.penup()

    # if 10 dots printed, start new line
    if dot_count % 10 == 0:
        x = -250
        y += 50
        joe.goto(x, y)
        continue

    joe.forward(50)
    x += 50
    joe.pendown()


screen = Screen()
screen.exitonclick()