from turtle import Screen,Turtle
from ball import Ball
from player import Player
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=1200,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
t = Turtle()
t.color("white")
t.penup()
t.hideturtle()
t.goto(0, -280)
t.pendown()
t.pensize(5)
while t.ycor() <= 280:
    t.goto(0, t.ycor() + 20)
    t.penup()
    t.goto(0, t.ycor() + 20)
    t.pendown()


POS = [(-580,0),(580,0)]
screen.tracer(0)


ball = Ball()
scoreboard = Scoreboard()

p1 = Player()
p1.goto(POS[0])
p2 = Player()
p2.goto(POS[1])

screen.listen()
screen.onkeypress(p1.up,"w")
screen.onkeypress(p1.down,"s")
screen.onkeypress(p2.up,"Up")
screen.onkeypress(p2.down,"Down")


game = True
while game:
    time.sleep(ball.slp)
    screen.update()
    ball.move()

    x = ball.xcor()
    y = ball.ycor()
    if p1.distance(x,y)<=30 and x <= -540:
        ball.bounce_p()
    if p2.distance(x,y)<=30 and x >= 560:
        ball.bounce_p()

    # if x >= 590 or x <= -590:
    #     screen.clear()
    #     screen.bgcolor("black")
    #     scoreboard.game_over()
    #     break
    if x>=590:
        scoreboard.score(0)
        ball.reset()
    elif x<=-590:
        scoreboard.score(1)
        ball.reset()

    if y >= 280 or y <= -280:
        ball.bounce_w()





screen.exitonclick()