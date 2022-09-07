from turtle import Turtle

X_POS = 0
Y_POS = 0

WIDTH = 20
HEIGHT = 20

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(X_POS, Y_POS)

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)