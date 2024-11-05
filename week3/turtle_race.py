from turtle import Turtle, Screen
import random


game_started = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y_value = -80
colour_num = 0

for turtle in colours:
    
    turtle = Turtle(shape="turtle")
    turtle.color(colours[colour_num])
    turtle.penup()
    turtle.goto(-230, y_value)
    all_turtles.append(turtle) # Add each turtle to the list
    y_value += 20
    colour_num += 1


if user_bet:
    game_started = True

while game_started == True:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            game_started = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won, {winning_colour} turtle won!")
            else:
                print(f"You've lost, {winning_colour} turtle won!")
        turtle_distance = random.randint(1, 10)
        turtle.forward(turtle_distance)

        
    



screen.exitonclick()