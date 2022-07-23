from turtle import Turtle
from random import random, randint, choice
import time


CAR_FPS = 1/30
CAR_Y = [-200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
CAR_DIRECTION = [1, -1]

class Car(Turtle):
    def __init__(self, difficulty):
        super(Car).__init__()
        self.car_list = []
        self.last_timestamp = time.monotonic()
        self.allowed_timestamp = self.last_timestamp + CAR_FPS
        self.difficulty = difficulty
        self.move_multiplier = 1
        for car in range(0, difficulty):
            self.car_list.append(self.new_car())

    def new_car(self):
        self = Turtle(shape="square")
        self.turtlesize(stretch_len=3, stretch_wid=1)
        self.color(random()**0.5, random()**0.5, random()**0.5)
        self.penup()

        self.move_permission = False
        self.move_speed = randint(2, 7)
        self.row = CAR_Y.pop(randint(0, len(CAR_Y)-1))
        self.direction = choice(CAR_DIRECTION)
        if self.direction == 1:
            self.goto(-210, self.row)
            self.setheading(0)
        elif self.direction == -1:
            self.goto(210, self.row)
            self.setheading(-180)
        return self

    def time_to_move(self):
        if time.monotonic() > self.allowed_timestamp:
            self.allowed_timestamp += CAR_FPS
            self.move_cars()

    def move_cars(self):

        for cars in self.car_list:
            if cars.xcor() > 225 or cars.xcor() < -225:
                self.despawn(cars)
                while len(self.car_list) < self.difficulty:
                    self.car_list.append(self.new_car())
            cars.forward(cars.move_speed * self.move_multiplier)

    def despawn(self, cars):
        CAR_Y.append(cars.ycor())
        self.car_list.remove(cars)
