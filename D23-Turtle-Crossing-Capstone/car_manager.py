from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5   # move per refresh
MOVE_INCREMENT = 10  # move distance increment on each level up
CAR_X_COR = 300


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        rand_chance = random.randint(1, 6)
        if rand_chance == 5:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            rand_y = random.randint(-250, 250)
            new_car.goto(CAR_X_COR, rand_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def collision(self, player_x, player_y):
        for car in self.all_cars:
            if car.distance(player_x, player_y) < 20:
                return True

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
