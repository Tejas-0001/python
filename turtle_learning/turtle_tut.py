import random
import turtle
from turtle import Turtle,Screen
import random
turtle.colormode(255)

"""This setting colormode to 255 is necessary to allow random colors otherwise you will be limited to colorspace defined in tkinter"""


# colors = ["red","blue","green","black","pink","violet","yellow","brown"]
# directions = [0,90,180.270]
t = Turtle()
t.shape("turtle")
# t.pensize(5)
t.speed("fastest")

# for i in range(200):
#     t.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
#     t.forward(30)
#     t.setheading(random.choice(directions))

def spirograph(angle):
    for _ in range(int(360/angle)):
        t.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        t.circle(100)
        t.setheading(t.heading()+angle)

spirograph(5)






screen = Screen()
screen.exitonclick()

# tup = (0.2, 0.8, 0.55)
# t.pencolor(tup)
#
# t.forward(50)
# t.pencolor("yellow")
# t.forward(50)
# t.pencolor("black")
# t.forward(50)

# for i in range(5):
#     t.forward(10.0)
#     t.penup()
#     t.forward(10.0)
#     t.pendown()
# t.begin_fill()
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.end_fill()

# for i in range(3,11):
#     t.pencolor(colors[i-3])
#     k  = i
#     while k:
#         t.forward(100)
#         t.right(360/i)
#         k -=1

# while 1:
#     choice = random.randint(1,3)
#     c = random.choice(colors)
#     t.pencolor(c)
#     if choice == 1:
#         t.right(90)
#         t.forward(20)
#     elif choice == 2:
#         t.forward(20)
#     else:
#         t.right(270)
#         t.forward(20)