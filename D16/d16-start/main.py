

# import turtle
from turtle import Turtle, Screen

# Instantantiate object named timmy using Turtle() class in turtle library
# timmy = turtle.Turtle()
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("DeepPink2")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()