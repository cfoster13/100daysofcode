capitals = {
    "France": "Paris",
    "England": "London",
    "Germany": "Berlin"
}

travel_log = { #nested list in dictionary
    "France": ["Paris", "Lille", "Dijion"],
    "Germany": ["Stuttgart", "Berlin"],

}

#Printing Lille
print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

#Printing D
print(nested_list[2][1])

travel_log_dict = { #nested dict in dictionary
    "France": {
      "cities_visited": ["Paris", "Lille", "Dijion"],
      "total_visits": 12

    },
    "Germany": {
        "cities_visited": ["Stuttgart", "Berlin", "Hamburg"],
        "total_visits": 6
    },
}

# print hamburg

print(travel_log_dict["Germany"]["cities_visited"][2])