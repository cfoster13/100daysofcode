import coffee_machine_info
import math

espresso = coffee_machine_info.MENU["espresso"]
print(espresso)

has_entered_report = False
machine_on = True


def report(water, milk, coffee, money):
    coffee_machine_info.resources["water"] -= water
    coffee_machine_info.resources["milk"] -= milk
    coffee_machine_info.resources["coffee"] -= coffee
    coffee_machine_info.resources["money"] += money

    if has_entered_report:
        print(coffee_machine_info.resources)


def check_ingredient_amount(drink):
    ingredients = coffee_machine_info.MENU[drink]["ingredients"]
    for item, amount in ingredients.items(): # checks each entry the item and amount, .items is a method to return items in a dict
        if amount > coffee_machine_info.resources[item]:
            print(f"Unfortunately, the machine doesn't have enough {item}")
            return False
    print(f"There are sufficient ingredients to make your {drink}")
    return True

def serve_drink(drink):
    if check_ingredient_amount(drink): # checking if there are enough ingredients to make an espresso
        customer_coins = input_coins()
        if customer_coins > coffee_machine_info.MENU[drink]["cost"]:
            change_given = customer_coins - coffee_machine_info.MENU[drink]["cost"]
            print(f"Here is your {drink} with your change of ${round(change_given, 2)}") # To 2 decimal places
            # ADD PROFIT TO COFFEE MACHINE
        elif customer_coins == coffee_machine_info.MENU[drink]["cost"]:
            print(f"Here is your {drink}, no change to give you.")
            # ADD PROFIT TO COFFEE MACHINE
        else:
            amount_left = coffee_machine_info.MENU[drink]["cost"] - customer_coins
            print(f"Not enough money, you need {amount_left} more.")
            print(f"You have been refunded {customer_coins}.")



def input_coins(): # Takes coins from the user and converts them into dollars

    dollars = 0 # initalise
    quarters_inserted = int(input("Enter the amount of quarters: "))
    dimes_inserted = int(input("Enter the amount of dimes: "))
    nickles_inserted = int(input("Enter the amount of nickles: "))
    pennies_inserted = int(input("Enter the amount of pennies: "))

    dollars += quarters_inserted / 4
    dollars += dimes_inserted / 10
    dollars += nickles_inserted / 20
    dollars += pennies_inserted / 100

    return dollars

while machine_on:
    serve_customer = input("What would you like? (espresso/latte/cappuccino): ").lower() # Keep asking the user for drinks whilst machine is on


    if serve_customer == "report":
        has_entered_report = True
        report(0, 0, 0, 0)
    if serve_customer == "off":
        print("Turning coffee machine off...")
        machine_on = False # Turn the coffee machine off and exit loop
    if serve_customer == "espresso":
        serve_drink("espresso")
        report(coffee_machine_info.MENU["latte"]["ingredients"]["water"],
            coffee_machine_info.MENU["latte"]["ingredients"]["milk"], 
            coffee_machine_info.MENU["latte"]["ingredients"]["coffee"], 
            coffee_machine_info.MENU["latte"]["cost"])
    elif serve_customer == "latte":
        serve_drink("latte")
        report(coffee_machine_info.MENU["latte"]["ingredients"]["water"], 
               coffee_machine_info.MENU["latte"]["ingredients"]["milk"], 
               coffee_machine_info.MENU["latte"]["ingredients"]["coffee"], 
               coffee_machine_info.MENU["latte"]["cost"])
    elif serve_customer == "cappuccino":
        serve_drink("cappuccino")
        report(coffee_machine_info.MENU["latte"]["ingredients"]["water"], # Update the report with the used up ingredients from making the drink
               coffee_machine_info.MENU["latte"]["ingredients"]["milk"], 
               coffee_machine_info.MENU["latte"]["ingredients"]["coffee"], 
               coffee_machine_info.MENU["latte"]["cost"])

# Make a function to add ingredients to the coffee machine

