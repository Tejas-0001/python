# import turtle
#
# # START_POS = [(0,0),(-20,0),(-40,0)]  constants are declared this way in python
# class Snake:
#     body=[]
#     start_pos= [(0,0),(-20,0),(-40,0)]
#     # instead of defining these here statically define them in init
#
#     def __init__(self):
#         # self.body = []
#         for i in range(3):
#             t = turtle.Turtle("square")
#             t.color("white")
#             t.penup()
#             t.goto(Snake.start_pos[i])
#             Snake.body.append(t)
#
#     @staticmethod
#     def move():
#         for i in range(len(Snake.body)-1,0,-1):
#             x = Snake.body[i-1].xcor()
#             y = Snake.body[i-1].ycor()
#             Snake.body[i].goto(x,y)
#         Snake.body[0].forward(20)

from turtle import Turtle

START_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()

    def create_snake(self):
        for i in range(len(START_POSITIONS)):
            t = Turtle("square")
            t.color("white")
            t.penup()
            t.goto(START_POSITIONS[i])
            self.segments.append(t)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()
            self.segments[i].goto(x,y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def create_segment(self):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(self.segments[-1].position())
        self.segments.append(t)

    def reset(self):
        for body in self.segments:
            body.hideturtle()
        self.segments = []
        self.create_snake()


