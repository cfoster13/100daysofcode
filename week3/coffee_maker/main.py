from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create objects for drinks with their cost

latte = MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5)
espresso = MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5)
cappuccino = MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3)

#Creating objects

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
drinks_menu = Menu()
all_drinks = Menu()
is_on = True

# Ask the user what they would like and check if drink is on the menu
while is_on:

    print("You can order these drinks: ")
    print(all_drinks.get_items())
    choice = input("What drink would you like: ").lower()
    drinks_menu.find_drink(choice) # Look for the drink to check if it's on the menu

    if choice == "off":
        print("Coffee machine is turning off...")
        is_on = False
    elif choice == "report":
        coffee_maker.report() # print a report of the coffee maker
        money_machine.report() # print money
    else:
        drink = drinks_menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost): # make drink if enough resources
            coffee_maker.make_coffee(drink) # Only make coffee if person has enough money
    

    

    




