from tkinter import messagebox
import turtle
import pandas
import tkinter

screen = turtle.Screen()
screen.title("US States Game")
image = "week5/Guess_US_States/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read the csv file
# Check if state entered is valid
# Take the answer state to get the x, y coordinates
# Print the state name on the image

data = pandas.read_csv("week5/Guess_US_States/50_states.csv")

state_list = data.state.to_list()

guessed_states = [] 


while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)} / 50 Guess the State", prompt="Enter a State name: ").title()


    if answer_state in state_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        states_data = data[data.state == answer_state] # Checks the row equal to the answer state
        t.goto(states_data.x.item(), states_data.y.item()) # Goes to the x,y coords of the state row
        t.write(answer_state)

    else:
        messagebox.showinfo(f"{len(guessed_states)} / 50 Guess the State", "That's not a US State")


screen.mainloop()

