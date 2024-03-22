import time
from turtle import Screen,Turtle
from player import Player
import time

s = Screen()
s.setup(width=730,height=500)
s.bgpic(picname="blank_states_img.gif")

p = Player()
t = Turtle()
t.penup()
t.hideturtle()

while 1:
    time.sleep(1)
    g = s.textinput(f"{p.guessed_count}/{p.total_count} States correct","Guess state name")
    if g == "over":
        p.game_over()
        break
    op = p.guess(g)
    if type(op) is tuple:
        t.goto(op[1],op[2])
        t.write(op[0])
    else:
        t.goto(0,0)
        t.write(op,font=("Arial", 24, "normal"))
        time.sleep(1)
        t.undo()
    if p.guessed_count == p.total_count:
        t.clear()
        t.goto(0,0)
        t.write("Game Over\nWell Done",font=("Arial", 24, "normal"))
        time.sleep(2)
        break

# s.exitonclick()
