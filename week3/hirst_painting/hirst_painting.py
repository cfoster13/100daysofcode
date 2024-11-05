import colorgram
from turtle import Turtle, Screen
import turtle as t
import random

#Extracting colours from image
# colors = colorgram.extract('week3/hirst_painting/dots.PNG', 10)

# list_of_colors = []

# for color in colors:
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g

#     new_color = (r, b, g) 
#     list_of_colors.append(new_color)

# print(list_of_colors)



color_list = ((233, 241, 237), (240, 244, 247), (201, 110, 172), (153, 175, 186), (154, 196, 180), (196, 177, 163), (213, 116, 205), (208, 193, 179))

t.colormode(255) # Enables RGB 
tim = Turtle()


screen = Screen()
screen.setup(width = 800, height = 600)

# Move to the bottom-left corner
bottom_left_x = -screen.window_width() // 2 + 150
bottom_left_y = -screen.window_height() // 2 + 100
tim.penup()
starting_pos = tim.setposition(bottom_left_x, bottom_left_y)

# tim.goto() # Set turtle position to bottom left of the screen
# 10 by 10 dots, 20 in size and spaced by 50
# randomly select colours

# have a for loop for drawing 10 cirlces, 20 in size and spaced by 50
# then move the turtle up by 50

# 768 x 648

def draw_circle():
    tim.begin_fill()
    r = 10
    tim.speed("fastest")

    random_colour = random.choice(color_list)

    tim.pencolor(random_colour)
    tim.circle(r)
    tim.fillcolor(random_colour)
    tim.end_fill()

rows = 0

while rows < 10:

    for i in range(11):
        draw_circle()
        tim.penup()
        tim.forward(50)

    rows += 1

    bottom_left_y += 50
    tim.setposition(bottom_left_x, bottom_left_y)


t.done()


screen.exitonclick()


