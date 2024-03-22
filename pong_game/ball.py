import random
from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.setheading(random.randint(20,40))
        self.goto(0,0)
        self.speed("fastest")
        self.x = 20
        self.y = 20
        self.slp = 0.1

    def bounce_w(self):
        self.y*=-1

    def bounce_p(self):
        self.x*=-1
        self.slp *= 0.9

    def move(self):
        x = self.xcor() + self.x
        y = self.ycor() + self.y
        self.goto(x,y)

    def reset(self):
        self.goto(0,0)
        self.slp = 0.1
        self.bounce_p()


    # def collision_w(self):
    #     if 90>self.heading()>=0 or 270>self.heading()>=180:
    #         self.setheading(self.heading() - 90)
    #         self.forward(30)
    #     elif 360>self.heading()>=270 or 180>self.heading()>=90:
    #         self.setheading(self.heading() + 90)
    #         self.forward(30)
    #     else:
    #         self.setheading(self.heading()+180)
    #
    # def collision_p(self):
    #     if 90>self.heading()>0 or 270>self.heading()>180:
    #         self.setheading(self.heading() + 90)
    #         self.forward(30)
    #     elif 360>self.heading()>270 or 180>self.heading()>90:
    #         self.setheading(self.heading() - 90)
    #         self.forward(30)
    #     else:
    #         self.setheading(self.heading()+180)



