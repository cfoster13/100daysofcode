from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = [] # List to store all the cars
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def spawn_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        random_y_pos = random.randint(-260, 260)
        new_car.goto(300, random_y_pos)
        self.all_cars.append(new_car)
        

    def increase_speed(self): # Call when level up
        self.car_speed += STARTING_MOVE_DISTANCE

    def move(self):
        # Move each car in the list to the left
        for car in self.all_cars:
            car.goto(car.xcor() - self.car_speed, car.ycor())

    def check_collision(self, player):
        for car in self.all_cars: # Check if any car is within the distance to the player
            if car.distance(player) < 20:
                return True
        return False
    
    def clear_cars(self):
        for car in self.all_cars:
            car.hideturtle()
            car.clear()

        self.all_cars.clear()

    

    

       



    
