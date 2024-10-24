import random

correct_number = random.randint(1, 100) # randomly choose a number between 1-100
number_of_guesses = 0
has_won = False

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty_choice == "easy":
    number_of_guesses = 10
elif difficulty_choice == "hard":
    number_of_guesses = 5

while number_of_guesses > 0 and has_won == False:
    guessed_number = int(input("Make a guess: "))

    if guessed_number == correct_number:
        print("Well done you guessed the correct answer! ")
        has_won = True

    elif guessed_number > correct_number:
        print("Too high.")
        print("Guess again.")
        number_of_guesses -= 1
        print(f"You have {number_of_guesses} attempts remaining to guess the number.")

    elif guessed_number < correct_number:
        print("Too low.")
        print("Guess again.")
        number_of_guesses -= 1
        print(f"You have {number_of_guesses} attempts remaining to guess the number.")

if has_won == False:
    print("You have ran out of guesses.")
    print("Better luck next time.")


