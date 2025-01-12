from tkinter import *
import requests



def get_quote():
    response = requests.get("https://api.kanye.rest/") # Get the api
    response.raise_for_status() # Raise status errors

    data = response.json()["quote"] # Access the dictionary key
    canvas.itemconfig(quote_text, text=data)
    print(data)




window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="week8/kayne-quotes-api/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="text goes here", width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="week8/kayne-quotes-api/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()