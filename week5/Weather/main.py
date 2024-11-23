# with open('week5/Weather/weather_data.csv', "r") as weather_data:
#     data = weather_data.readlines()

# print(data)

import csv
import pandas
import math

# with open('week5/Weather/weather_data.csv') as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         print(row)
#         temperatures.append(row[1])

#     temperatures.remove('temp')
    

#     for i in range(len(temperatures)):
#         temperatures[i] = int(temperatures[i])


#     print(temperatures)

data = pandas.read_csv('week5/Weather/weather_data.csv')
#print(data["temp"])

temp_list = data["temp"].to_list()
print(temp_list)

sum = 0

for temperatures in temp_list: # Or use python SUM method / Series.mean
    sum += temperatures

average = round(sum / len(temp_list), 2)

print(f"The average temperature is: {average}")

# Get max value from using panda documentation

print(data["temp"].max())
max_temp = data.temp.max()

# Print the data with the highest temp

print(data[data.temp == max_temp]) # Filter condition 

# Get Mondays temp then convert to Fahrenheit

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0] # Must specify the row number
fahrenheit = (monday_temp * 9/5) + 32

print(f"Monday's temperature was {monday_temp} which is {fahrenheit} in Fahrenheit")
