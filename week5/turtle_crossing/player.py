from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, scoreboard, car_manager):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90) 
        self.goto(STARTING_POSITION)
        self.scoreboard = scoreboard # Single scoreboard which can be manipluated many times
        self.car_manager = car_manager

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE

        self.goto(0, new_y)

        if self.distance(0, FINISH_LINE_Y) < 5:  # 5 is a tolerance value
            self.goto(STARTING_POSITION)
            self.scoreboard.level_up()
            self.car_manager.clear_cars()
            print("increasing speed")
            self.car_manager.increase_speed()
            print(self.car_manager.car_speed)

        

    def reset_position(self):
        self.goto(STARTING_POSITION)

 

