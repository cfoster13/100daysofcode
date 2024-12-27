from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10) 
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #

#When user presses the add button, put email, password, wesbite into a txt file
#Then delete website and password entry info

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    
    
    if len(website) > 0 and len(password) > 0:

        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                               f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            f = open("week7/PasswordManager/info.txt", "a")
            f.write(f"{website} | {email} | {password}\n")
            f.close()
            website_entry.delete(0, END)
            pass_entry.delete(0, END)

    else:
        messagebox.showwarning(title="Warning", message="You cannot leave fields empty!")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="week7/PasswordManager/logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

#Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=1)
email_entry.insert(0, "chayefoster@icloud.com")

pass_entry = Entry(width=35)
pass_entry.grid(column=1, row=3, columnspan=1)

#Buttons

generate_pass = Button(text="Generate Password", command=generate_password)
generate_pass.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=1)


window.mainloop()