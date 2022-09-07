from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Game Constants
L_PADDLE_COR = (-350, 0)
R_PADDLE_COR = (350, 0)
X_LEFT = -400
X_RIGHT = 400
Y_TOP = 280
Y_BOTTOM = -280

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

    # Detect collision with wall
    if ball.ycor() > Y_TOP or ball.ycor() < Y_BOTTOM:
        ball.wall_bounce()

    # Detect collision with right paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.paddle_bounce()

    # Detect when R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()

    # Detect when L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()

screen.exitonclick()