import random


fifty_percent_chance = random.randint(1, 2)

choice = input("Do you choose heads or tails? ").lower()

if fifty_percent_chance == 1 and choice == "heads":
    print("Well done, it was heads!")
elif fifty_percent_chance == 2 and choice == "tails":
    print("Well done, it was tails!")

else:
    if fifty_percent_chance == 1:
        result = "heads"
    elif fifty_percent_chance == 2:
        result = "tails"
    print(f"Unfortunately it was {result}")