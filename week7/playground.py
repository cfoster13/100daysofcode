from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)


my_label["text"] = "New Text"
my_label.config(text="New Text")



button = Button(text="Click Me", command=button_clicked)
button.grid(column=1,row=1)

button2 = Button(text="new button")
button2.grid(column=2, row=0)


input = Entry(width=10)
input.grid(column=3, row=2)

# 3 rows and 4 columns
# Label: 0,0
# Button: 1, 1
# New Button: 0, 2
# Entry: 




window.mainloop()

