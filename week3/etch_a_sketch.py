from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def rotate_counter_clockwise():
    tim.left(20)

def rotate_clockwise():
    tim.right(20)

def clear_screen():
    screen.reset() # Clears the screen and resets turtle back to original position

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_counter_clockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()