from turtle import Turtle
# screen = Screen()
# screen.bgcolor("black")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.s1 = 0
        self.s2 = 0
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.write(f"{self.s1}      {self.s2}", move=False, align="center", font=("Arial", 24, "normal"))


    def score(self,n):
        if n == 0:
            self.s1 +=1
        else:
            self.s2 +=1
        self.clear()
        self.write(f"{self.s1}      {self.s2}", move=False, align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over\n      {self.s1} - {self.s2}", move=False, align="center", font=("Arial", 24, "normal"))




# t = Scoreboard()
# screen.exitonclick()