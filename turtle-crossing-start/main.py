import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle crossing")
screen.listen()

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager(5)

screen.onkey(player.move,"w")




game_is_on = True
while game_is_on:
    time.sleep(0.09)
    screen.update()

    if player.ycor() == 270:
        for i in range(10):
            car_manager.create()
        scoreboard.level()
        # time.sleep(2)
        player.goto(0,-280)

    for cars in car_manager.all:
        if player.distance(cars.xcor(),cars.ycor()) < 20:
            scoreboard.game_over()
            game_is_on = False
            break
        if cars.xcor() >= -280:
            car_manager.move(cars)
        else:
            cars.hideturtle()
            car_manager.all.pop(car_manager.all.index(cars))
            car_manager.create_x()

screen.exitonclick()
