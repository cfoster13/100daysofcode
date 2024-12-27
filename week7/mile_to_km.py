from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)

def button_clicked():
    miles = int(miles_entry.get())
    km = miles * 1.609
    km_label_amount.config(text=km)


my_label = Label(text="is equal to")
my_label.grid(column=0,row=1)

my_label_miles = Label(text="Miles")
my_label_miles.grid(column=2, row=0)

my_label_km = Label(text="Km")
my_label_km.grid(column=2, row=1)

miles_entry = Entry(text=0)
miles_entry.grid(column=1, row=0)

km_label_amount = Label(text=0)
km_label_amount.grid(column=1, row=1)

calculate = Button(text="Calculate", command=button_clicked)
calculate.grid(column=1, row=2)

# Miles to Km: 1 mile = 1.609km




window.mainloop()