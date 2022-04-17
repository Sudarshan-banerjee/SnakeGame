from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("My Snake game")
screen.tracer(0)            #Tracer sets off the contents in the screen

scorecard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scorecard.increase_score()
        print('num num num')

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scorecard.game_over()
        game_on = False

    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            scorecard.game_over()
            game_on = False
screen.exitonclick()