import time
from turtle import Turtle, Screen
from frog import Frog
from car import Car

difficulty = 6
screen = Screen()
screen.setup(width=400, height=600)
screen.tracer(0)
screen.bgcolor(0.1, 0.1, 0.1)
screen.listen()
start = Turtle("square")
start.turtlesize(stretch_len=50, stretch_wid=3)
start.penup()
start.goto(x=0, y=-260)
start.color(0.5, 0.5, 0.4)
finish = Turtle("square")
finish.turtlesize(stretch_len=50, stretch_wid=3)
finish.penup()
finish.goto(x=0, y=290)
finish.color(0.2, 0.6, 0.2)
text = Turtle()
text.hideturtle()
text.penup()
text.color(0.9, 0.9, 0.9)
level_number = 1


def level():
    text.clear()
    text.goto(x=120, y=220)
    text.write(arg=f"Level {level_number}", align="center", font=("Courier", 20, "normal"))


def game_over():
    text.goto(0, 0)
    text.write(arg="GAME OVER", align="center", font=("Courier", 20, "normal"))


def esc():
    screen.bye()


screen.onkey(esc, "Escape")

frog = Frog()
car = Car(difficulty)


def update_screen():
    frog.time_to_move()
    car.time_to_move()
    screen.update()


screen.onkeypress(frog.up, "Up")
screen.onkeypress(frog.down, "Down")
screen.onkeypress(frog.left, "Left")
screen.onkeypress(frog.right, "Right")
screen.onkey(esc, "Escape")

level()
not_dead = True
while not_dead:
    time.sleep(0.01)
    if frog.splat(car.car_list):
        game_over()
        not_dead = False
    update_screen()
    if frog.ycor() > 260:
        level_number += 1
        level()
        frog.goto(0, -280)
        if level_number < 5:
            car.difficulty += 5
        else:
            car.move_multiplier *= 1.2
update_screen()
screen.exitonclick()
