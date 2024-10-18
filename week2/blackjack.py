import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def game_loop():

    player_card_one = random.choice(cards)
    player_card_two = random.choice(cards)
    players_cards = [player_card_one, player_card_two]

    computer_card_one = random.choice(cards)
    computer_card_two = random.choice(cards)
    computer_cards = [computer_card_one, computer_card_two]

    has_won = False

    def winner():
        total_player_score = sum(players_cards)
        total_computer_score = sum(computer_cards)

        if total_player_score == 21 and total_computer_score != 21:
            print("Well done you've reached 21!")
            print(f"Computer had these cards: {computer_cards}")
            print(f"Computer score: {total_computer_score}") # Need to total up all computer cards

        elif total_player_score > total_computer_score and total_player_score < 21:
            print("Well done you were closest to 21!")
            print(f"Computer had these cards: {computer_cards}")
            print(f"Computer score: {total_computer_score}") # Need to total up all computer cards


        elif total_player_score == total_computer_score:
            print("It's a draw!")
            print(f"Computer had these cards: {computer_cards}")
            

        else:
            print(f"Computer had these cards: {computer_cards}")
            print(f"Computer score: {total_computer_score}") # Need to total up all computer cards
            print("You lose!")


    print(f"Your cards are: {players_cards}")
    print(f"Score: {sum(players_cards)}")
    print(f"The computer's first card is: [{computer_cards[0]}]")

    computer_visible_cards = 1 # Computer starts with one card visible to the player

    while not has_won: #Player and computer still in game
        play_again = input("Enter y for another card or n to pass: ").lower()
        
        if play_again == "y":
            players_cards.append(random.choice(cards)) # Randomly add a new card to the player's hand
            print(f"Your cards are: {players_cards}")
            player_card_score = sum(players_cards) # Adding all player cards together
            computer_card_score = sum(computer_cards)
            print(f"Your new score is now {player_card_score}")
            # Add new card to computers hand and display the next card
            computer_cards.append(random.choice(cards))
            computer_visible_cards += 1

            print("The computer's cards are: [", end="")
            for i in range(computer_visible_cards):
                if i == computer_visible_cards - 1:
                    print(computer_cards[i], end="") # Trying to only display the first two cards
                else:
                    print(computer_cards[i], end=", ")
            print("]")

            # Check if player has won or gone over
            if player_card_score > 21:
                print("You have gone over 21! You lose.")
                has_won = True
            elif player_card_score == 21:
                print("You've hit 21!")
                winner()
                has_won = True
            

        elif play_again == "n":
            print(f"The computer's cards are: {computer_cards}")
            print(f"Computer's score: {sum(computer_cards)}")
            winner()
            has_won = True


while True:
    ask_to_play = input("Would you like to play a game of blackjack? y/n ").lower()

    if ask_to_play == "y":
        game_loop()
    elif ask_to_play == "n":
        print("Thank you for playing!")




