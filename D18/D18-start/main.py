import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
directions = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

tim = Turtle()
tim.shape("turtle")
tim.color("dark green")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

# Challenge 1
# for i in range(4):
#     tim.right(90)
#     tim.forward(50)

# Challenge 2
# for _ in range(25):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Challenge 3
# Draw Shapes
# for shape_sides in range(3, 11):
#     angle = 360/shape_sides
#     for side in range(shape_sides):
#         tim.color(random_color())
#         tim.right(angle)
#         tim.forward((100))

# Challenge 4
# Random Walk
# tim.speed("fastest")
# tim.pensize(10)
# for _ in range (200):
#     tim.setheading(random.choice(directions))
#     tim.color(random_color())
#     tim.forward(30)

# Challenge 5
# Draw a no. of circle w/ radius 100
tim.speed("fastest")
for angle in range(0, 360, 5):
    tim.setheading(angle)
    tim.color(random_color())
    tim.circle(100)




screen = Screen()
screen.exitonclick()