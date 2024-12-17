import pandas
import turtle


# Country, Capital City, Latitude, Longitude

screen = turtle.Screen()
screen.setup(width=1200, height=607)
screen.title("Countries in the World")
image = "week5/Guess_Country_Capitals/world_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("week5/Guess_Country_Capitals/country-capital.csv")

def on_click(x, y):
    print(f"You clicked x:{x}, y:{y}")

country_list = data.Country.to_list()
capital_list = data["Capital City"].to_list()

guessed_countries = []

screen.onclick(on_click)

answer_country = screen.textinput("Guess the country", "Enter a country:")

if answer_country in country_list:
    guessed_countries.append(answer_country)
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    country_data = data[data.Country == answer_country]
    t.goto(country_data.Latitude.item(), country_data.Longitude.item())
    t.write(answer_country, align="center")

answer_capital = screen.textinput(f"Capital city of {answer_country}", "Enter the capital:")

if answer_capital in capital_list:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.color("blue")
    city_data = data[data["Capital City"] == answer_capital]
    t.goto(country_data.Latitude.item(), country_data.Longitude.item() - 10)
    t.write(answer_capital, align="center")

else:
    print("wrong capital city")

    


screen.mainloop()