from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)] # Positions of squares
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snakes.append(snake)

    def extend(self):
        self.add_segment(self.snakes[-1].position())


    def move(self):
        for snake_num in range(len(self.snakes) - 1, 0, -1): # Accesses the length of the snake and goes from back to front
            new_x = self.snakes[snake_num - 1].xcor() # New coordinates are set from the second to last square
            new_y = self.snakes[snake_num - 1].ycor()
            self.snakes[snake_num].goto(new_x, new_y) # Segment new location goes to the square in front

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)





    
    