from turtle import Screen
import time,random
from snake import Snake
from food import Food
from  scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

while 1:
    game_on = 1
    while game_on:
        screen.update()
        time.sleep(0.09)
        snake.move()

        x = snake.segments[0].xcor()
        y = snake.segments[0].ycor()
        if x <= -295 or x >= 295 or y >= 295 or y <= -295:
            game_on = 0

        for i in range(1,len(snake.segments)-1,1):
            if snake.segments[0].distance(snake.segments[i]) < 10:
                game_on = 0

        if snake.segments[0].distance(food) <= 15:
            snake.create_segment()
            scoreboard.score()
            while 1:
                f = 0
                food.refresh()
                x = food.xcor()
                y = food.ycor()
                for i in snake.segments:
                    if i.xcor() == x and i.ycor() == y:
                        f = 1
                        break
                if f == 1:
                    continue
                else:
                    break

    scoreboard.game_over()
    screen.update()
    time.sleep(1)
    scoreboard.score()
    snake.reset()

screen.exitonclick()