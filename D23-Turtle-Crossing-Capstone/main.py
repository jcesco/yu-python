import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Generate and move cars
    car_manager.generate_car()
    car_manager.move_cars()

    # Detect car collision
    squish = car_manager.collision(player.xcor(), player.ycor())
    if squish:
        game_is_on = False
        scoreboard.game_over()

    # Detect if player beat level, reset position and speed up cars
    if player.ycor() > 250:
        print("Winner")
        player.start_position()
        car_manager.speed_up()
        scoreboard.level_up()

screen.exitonclick()
