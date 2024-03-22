from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid= 3,stretch_len=0.7)
        self.penup()
        self.speed("fastest")

    def up(self):
        x = self.xcor()
        y = self.ycor()
        if y <= 280:
            self.goto(x,y+30)

    def down(self):
        x = self.xcor()
        y = self.ycor()
        if y >= -280:
            self.goto(x, y - 30)