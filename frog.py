from turtle import Turtle
from random import random
import time
from car import Car

MOVE_AMOUNT = 10
FROG_FPS = 1/10


class Frog(Turtle):
    def __init__(self):
        super(Frog, self).__init__()
        self.shape("turtle")
        self.color(random()**0.5, random()**0.5, random()**0.5)
        self.penup()
        self.goto(0, -280)
        self.setheading(90)
        self.last_timestamp = time.monotonic()
        self.allowed_timestamp = self.last_timestamp + FROG_FPS
        self.move_permission = False

    def time_to_move(self):
        if time.monotonic() > self.allowed_timestamp:
            self.allowed_timestamp += FROG_FPS
            self.move_permission = True

    def up(self):
        if self.move_permission:
            self.forward(MOVE_AMOUNT)
        self.move_permission = False

    def down(self):
        if self.ycor() > -290 and self.move_permission:
            self.back(MOVE_AMOUNT)
        self.move_permission = False

    def left(self):
        if self.xcor() < -290:
            pass
        elif self.move_permission:
            self.goto(self.xcor() - MOVE_AMOUNT, self.ycor())
            self.move_permission = False

    def right(self):
        if self.xcor() < 290 and self.move_permission:
            self.goto(self.xcor() + MOVE_AMOUNT, self.ycor())
            self.move_permission = False

    def splat(self, car_list):
        for cars in car_list:
            if self.distance(cars) < 20:
                return True
