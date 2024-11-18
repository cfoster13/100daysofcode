import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake() # Creating snake
food = Food() # Creating food
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    #scoreboard.write()
    snake.move() # Moving the snake

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score() # Add one to score

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.snakes[1:]: # Slicing every snake segment apart from the first one
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()



screen.exitonclick()