from turtle import Turtle, Screen
import turtle as t
import random

tim = Turtle()
t.colormode(255)

tim.shape("turtle")
tim.color("red")

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    colour_tuple = (r, g, b)

    return colour_tuple


def draw_square():
    for i in range(4): # Draw a square
        tim.forward(100)
        tim.left(90)

def draw_dashed_line():
    for i in range(10):
        tim.pendown()
        tim.forward(10)
        tim.penup()
        tim.forward(10)


def draw_shapes():
    number_of_sides = 3 # Start off with triangle
    
    while number_of_sides <= 10: # Draw every shape up to a decagon
        angle = 360 / number_of_sides
        pen_colour = random_colour() # Choose a random pen colour for each shape
        tim.pencolor(pen_colour)
        for i in range(number_of_sides):
            tim.forward(100)
            tim.left(angle)
        number_of_sides += 1

is_walking = True


# Change the pen size
# Draw a random walk, different directions with random colours

def random_walk():
    tim.pensize(10)
    tim.speed(10)
    while is_walking:
        tim.pencolor(random_colour())
        direction = [0, 90, 180, 270]
        tim.forward(25)
        tim.setheading(random.choice(direction))


def draw_circle():
    r = 100
    tim.speed("fastest")
    current_heading = tim.heading()
    rotation_angle = 5
    
    

    while True:
        tim.pencolor(random_colour())
        tim.circle(r)
        tim.setheading(tim.heading() + rotation_angle)
        
        #Stop if turtle has gone full 360 degrees

        if abs(tim.heading() - current_heading) < rotation_angle:
            break


draw_circle()

screen = Screen()
screen.exitonclick()