from turtle import Turtle, Screen

joe = Turtle()
screen = Screen()


def move_forward():
    joe.forward(10)


def move_backward():
    joe.backward(10)


def rotate_ccw():
    current_heading = joe.heading()
    new_heading = current_heading + 10
    joe.setheading(new_heading)


def rotate_cw():
    current_heading = joe.heading()
    new_heading = current_heading - 10
    joe.setheading(new_heading)


def clear_drawing():
    joe.reset()


# turtle.list - Set focus on TurtleScreen (in order to collect key-events). Dummy arguments are provided in order to
# be able to pass listen() to the onclick method.
# https://docs.python.org/3/library/turtle.html#turtle.listen
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=rotate_ccw)
screen.onkey(key="d", fun=rotate_cw)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()

