from turtle import Turtle

FONT = ("Courier", 18, "normal")
LEVEL_POSITION = (-280, 260)
ORIGIN = (0, 0)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(LEVEL_POSITION)
        self.write_score()

    def level_up(self):
        self.level += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(ORIGIN)
        self.write("GAME OVER", align="center", font=FONT)
