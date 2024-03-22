# import random
# import turtle
# turtle.colormode(255)
# from turtle import Turtle,Screen
# color = ["red","orange","yellow","green","blue","purple"]
# screen=Screen()
# screen.setup(width=500,height=400)
# t1 = Turtle("turtle")
# t1.color(color[0])
# t2 = Turtle("turtle")
# t2.color(color[1])
# t3 = Turtle("turtle")
# t3.color(color[2])
# t4 = Turtle("turtle")
# t4.color(color[3])
# t5 = Turtle("turtle")
# t5.color(color[4])
# t6 = Turtle("turtle")
# t6.color(color[5])
#
# choice = screen.textinput(title="Turtle Race",prompt="Enter the color of turtle which you think will win")
#
# t1.penup()
# t2.penup()
# t3.penup()
# t4.penup()
# t5.penup()
# t6.penup()
#
# t1.goto(-230,-100)
# t2.goto(-230,-60)
# t3.goto(-230,-20)
# t4.goto(-230,20)
# t5.goto(-230,60)
# t6.goto(-230,100)
#
#
#
# while 1:
#     t1.goto(t1.xcor() + random.randint(1, 10), -100)
#     t2.goto(t2.xcor() + random.randint(1, 10), -60)
#     t3.goto(t3.xcor() + random.randint(1, 10), -20)
#     t4.goto(t4.xcor() + random.randint(1, 10), 20)
#     t5.goto(t5.xcor() + random.randint(1, 10), 60)
#     t6.goto(t6.xcor() + random.randint(1, 10), 100)
#     if t1.xcor()>=230:
#         winner = color[0]
#         print("race finished")
#         print(f"{winner} turtle won the race !!")
#         break
#     elif t2.xcor()>=230:
#         winner = color[1]
#         print("race finished")
#         print(f"{winner} turtle won the race !!")
#         break
#     elif t3.xcor()>=230:
#         winner = color[2]
#         print("race finished")
#         print(f"{winner} turtle won the race !!")
#         break
#     elif t4.xcor()>=230:
#         winner = color[3]
#         print("race finished")
#         print(f"{winner} turtle won the race !!")
#         break
#     elif t5.xcor()>=230:
#         winner = color[4]
#         print("race finished")
#         print(f"{winner} turtle won the race !!")
#         break
#     elif t6.xcor()>=230:
#         winner = color[5]
#         print("race finished")
#         print(f"{winner} turtle won the race !!")
#         break
#
# if choice == winner:
#     print("\nYou win !!")
# else:
#     print("\nYou lose !")
#
# screen.exitonclick()

import random
from turtle import Turtle,Screen
color = ["red","orange","yellow","green","blue","purple"]
screen = Screen()
screen.setup(width=500,height=400)
start_pos = [-100,-60,-20,20,60,100]
racers = []
for i in range(6):
    t = Turtle(shape="turtle")
    t.color(color[i])
    t.penup()
    t.goto(-230,start_pos[i])
    t.speed("fastest")
    racers.append(t)

bet = screen.textinput(title="Turtle Race",prompt="Pick the color of turtle whom you wanna bet on :")
race = "on"

while race == "on":
    for i in range(6):
        distance = random.randint(1,10)
        racers[i].forward(distance)
        if racers[i].xcor() > 230:
            if racers[i].pencolor() == bet:
                print(f"You won the bet!! {racers[i].pencolor()} turtle won the race!!")
            else:
                print(f"You lost the bet!! {racers[i].pencolor()} turtle won the race!!")
            race = "off"



screen.exitonclick()

