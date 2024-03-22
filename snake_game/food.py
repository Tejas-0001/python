from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
        # flag = 1
        # while flag:

            # for i in snake.Snake().segments:
            #     if i.xcor() != x and i.ycor() != y:
            #         continue
            #     else:
            #         flag = 0
            #         break
            # if flag == 0:
            #     flag = 1
            # else:
            #     self.goto(x,y)
            #     flag = 0