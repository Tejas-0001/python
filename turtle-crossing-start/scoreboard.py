from turtle import Turtle

FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-260,260)
        self.lvl = 1
        self.level()

    def level(self):
        self.clear()
        self.write(f"Lvl : {self.lvl}",align="left", font=FONT)
        self.lvl += 1

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)