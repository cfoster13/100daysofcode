import pandas

data = pandas.read_csv("week5/Guess_US_States/50_states.csv")



for i in range(5): 
    print(data.loc[i,'state'], data.loc[i, 'x'], data.loc[i, 'y']) # Print the first 5 states
    


# Find rows where a specific condition is met: e.g. when y is less than 0 to show the south states of US
print(data.loc[data['y'] < 0])
