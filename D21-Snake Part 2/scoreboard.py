from turtle import Turtle
ALIGNMENT = "center"
FONT =("Arial", 24, "normal")

# Use https://docs.python.org/3/library/turtle.html#turtle.write
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("Pink")
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increment_score(self):
        self.score += 1
        self.update_scoreboard()
