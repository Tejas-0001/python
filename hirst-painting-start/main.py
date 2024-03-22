# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append((color.rgb.r,color.rgb.g,color.rgb.b))
#
# print(rgb_colors)
from turtle import Turtle,Screen
import random,turtle

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

t= Turtle()
screen = Screen()
t.speed("fastest")
turtle.colormode(255)
t.hideturtle()

for i in range(-250,251,50):
    for j in range(-250,251,50):
        t.penup()
        t.goto(i,j)
        # t.pendown()
        # t.color(random.choice(color_list))
        # t.begin_fill()
        # t.circle(10)
        # t.end_fill()
        t.dot(20,random.choice(color_list))









screen.exitonclick()