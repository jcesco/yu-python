from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5   # move per refresh
MOVE_INCREMENT = 10  # move distance increment on each level up


class CarManager:

    def __init__(self):
        self.new_car()


    def new_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.goto(100, 0)

    def move(self):
        pass

