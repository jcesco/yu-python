from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

L_PADDLE_COR = (-350, 0)
R_PADDLE_COR = (350, 0)

l_paddle = Paddle(L_PADDLE_COR)
r_paddle = Paddle(R_PADDLE_COR)
ball = Ball()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.1)

screen.exitonclick()