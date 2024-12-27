from tkinter import *
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

# Read CSV into a data frame

df = pd.read_csv('week7/Flash_Cards/data/spanish_words.csv')

# Convert dataframe to a dict

data_dict = df.to_dict(orient='records')
current_card = {}

def remove_card():
    global data_dict, current_card
    data_dict = [word for word in data_dict if word != current_card]
    new_data = pd.DataFrame(data_dict)
    new_data.to_csv('week7/Flash_Cards/data/remaining_words.csv', index=False)

    if data_dict:
        random_word()

def random_word():
    global current_card, flip_timer # Update the word on the canvas
    window.after_cancel(flip_timer) # cancel the 3 second timer for the new card
    current_card = random.choice(data_dict) # Pick random dict
    canvas.itemconfig(card_image, image=front_card_image) # Reset to front image
    canvas.itemconfig(language_text, text="Spanish", fill="black")  # Update the language label
    canvas.itemconfig(word_text, text=current_card["Spanish"], fill="black")  # Update the word text
    window.after(3000, func=flip_card)
    
def flip_card():
    global current_card
    # display english translation of the word
    # change image to the back and change title and text to white
    canvas.itemconfig(card_image, image=back_card_image)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


   


# --------------------- UI SETUP -------------------


window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flash Cards")


canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_card_image = PhotoImage(file="week7/Flash_Cards/images/card_front.png")
back_card_image = PhotoImage(file="week7/Flash_Cards/images/card_back.png")
card_image = canvas.create_image(400, 263, image=front_card_image)
canvas.grid(column=0, row=0, columnspan=2)


flip_timer = window.after(3000, flip_card)

# Text

language_text = canvas.create_text(400, 150, text="Spanish", font=(FONT_NAME, 40, "italic"))
canvas.grid(column=0, row=0, columnspan=2)

word_text = canvas.create_text(400, 263, text="Hola", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
incorrect_button_image = PhotoImage(file="week7/Flash_Cards/images/wrong.png")
incorrect_button = Button(image=incorrect_button_image, highlightthickness=0, command=random_word)
incorrect_button.grid(column=0, row=1)

correct_button_image = PhotoImage(file="week7/Flash_Cards/images/right.png")
correct_button = Button(image=correct_button_image, highlightthickness=0, command=remove_card)
correct_button.grid(column=1, row=1)

random_word()


window.mainloop()

