import turtle

t=turtle.Turtle()
screen = turtle.Screen()
t.speed("fastest")


def forward():
    t.forward(50)

def backward():
    t.setheading(180)
    t.forward(50)

def left():
    t.left(10)

def right():
    t.right(10)


def clear():
    t.reset() 

turtle.listen()

turtle.onkey(forward,"w")
turtle.onkey(left,"a")
turtle.onkey(right,"d")
turtle.onkey(backward,"s")
turtle.onkey(clear,"c")

screen.exitonclick()