from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.curr_score = 0
        with open("high_score.txt") as score:
            self.high_score = int(score.read())
        self.write(f"Score : {self.curr_score} High Score : {self.high_score}", move=False, align="center", font=("Arial", 16, "normal"))

    def score(self):
        self.clear()
        self.curr_score += 1
        self.write(f"Score : {self.curr_score} High Score : {self.high_score}", move = False, align="center", font=("Arial",16,"normal"))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over\n Score : {self.curr_score}\nHigh Score : {self.high_score}", move=False, align="center", font=("Arial", 16, "normal"))

        if self.curr_score > self.high_score:
            self.high_score = self.curr_score
            with open("High_score.txt","w") as score:
                score.write(f"{self.curr_score}")

        self.goto(0, 260)
        self.curr_score = -1



