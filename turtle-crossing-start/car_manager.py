COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random

class CarManager:

    def __init__(self,n):
        self.all = []
        for i in range(n):
            self.create()


    def create(self):
        t = Turtle()
        t.shape("square")
        t.shapesize(stretch_wid=1, stretch_len=2)
        t.color(random.choice(COLORS))
        t.penup()
        t.speed("slowest")
        t.goto(random.randint(-300, 300), random.randint(-220, 260))
        self.all.append(t)

    def create_x(self):
        t = Turtle()
        t.shape("square")
        t.shapesize(stretch_wid=1, stretch_len=2)
        t.color(random.choice(COLORS))
        t.penup()
        t.speed("slowest")
        t.goto(random.randint(280, 300), random.randint(-220, 260))
        self.all.append(t)


    @staticmethod
    def move(car):
        car.goto(car.xcor() - MOVE_INCREMENT, car.ycor())