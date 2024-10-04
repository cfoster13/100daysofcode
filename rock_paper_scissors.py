import random

player_choice = input("Enter rock, paper or scissors: ").lower()

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)

if computer_choice == options[0] and player_choice == "paper":
    print(f"Computer chose {computer_choice}") # ADD ART
    print(f"Well done you won! ")

elif computer_choice == options[1] and player_choice == "scissors":
    print(f"Computer chose {computer_choice}") # ADD ART
    print(f"Well done you won! ")

elif computer_choice == options[2] and player_choice == "rock":
    print(f"Computer chose {computer_choice}") # ADD ART
    print(f"Well done you won! ")

else:
    print(f"Computer chose {computer_choice}") # ADD ART
    print(f"Unfortunately you lost ")