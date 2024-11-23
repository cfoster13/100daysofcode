import pandas

squirrel_data = pandas.read_csv("week5/Squirrels/Squirrel_Data.csv")

# Extract the data from the csv, Primary Fur Color and count the amount

color_data = squirrel_data["Primary Fur Color"]


color_count = {}


for colors in color_data:
    if colors not in color_count:
        color_count[colors] = 1 # Color added to dictionary with a value of 1
    else:
        color_count[colors] += 1 # If color already exists add 1 to the value



print(color_count)



