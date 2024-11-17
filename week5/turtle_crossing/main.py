import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
car_manager = CarManager()
turtle = Player(scoreboard, car_manager)



screen.listen()
screen.onkey(turtle.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Randomly generates cars
    if random.randint(1, 10) == 3:
        car_manager.spawn_car()

    # Move cars
    car_manager.move()

    # Detect collision with cars
    if car_manager.check_collision(turtle):
        print("Collision detected!")
        scoreboard.game_over()
        game_is_on = False # Call game over
        screen.exitonclick()


    
    


    

