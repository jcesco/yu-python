from turtle import Turtle

class StateTracker(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def update_map(self, state, x_cor, y_cor):
        self.setpos(0,0)
        self.goto(x_cor, y_cor)
        self.write(state)


