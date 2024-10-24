import higher_or_lower_game_data
import random


random_opponent_a = random.choice(higher_or_lower_game_data.data) # chooses a random block of data
random_opponent_b = random.choice(higher_or_lower_game_data.data)

follower_count_a = random_opponent_a["follower_count"] # Accessing the follower count data
follower_count_b = random_opponent_b["follower_count"]

player_score = 0 # Starting off
has_lost = False


def highest_followers(opponent_a, opponent_b):
    if opponent_a > opponent_b:
        return opponent_a
    else:
        return opponent_b
    

while has_lost == False:
    result = highest_followers(follower_count_a, follower_count_b)

    compare_a = (f"Compare A: {random_opponent_a["name"]}, a {random_opponent_a["description"]}, from {random_opponent_a["country"]}.")
    print(compare_a)
    compare_b = (f"Against B: {random_opponent_b["name"]}, a {random_opponent_b["description"]}, from {random_opponent_b["country"]}.")
    print(compare_b)

    ask_for_followers = input("Who has more followers? Type 'A' or 'B': ")

    if result == follower_count_a and ask_for_followers == "A":
        player_score += 1
        print(f"You're right! Current score: {player_score}.")
        random_opponent_b = random.choice(higher_or_lower_game_data.data) # Choosing a new B
        follower_count_b = random_opponent_b["follower_count"] # Update the following count
    elif result == follower_count_b and ask_for_followers == "B":
        player_score += 1
        print(f"You're right! Current score: {player_score}.")
        random_opponent_a = random_opponent_b # B becomes A
        follower_count_a = random_opponent_a["follower_count"]

        random_opponent_b = random.choice(higher_or_lower_game_data.data) # Choosing a new B
        follower_count_b = random_opponent_b["follower_count"]
    else:
        print(f"Sorry that's wrong. Final score: {player_score}.")
        has_lost = True # player loses the game




# randomly select a list in the array for opponent A
# Do the same for opponent B
# Ask the user who has more followers
# Compare the follower count key to find the highest
# if player guesses incorrectly end the game with their final score being displayed
# if the player guesses correctly add one to their score, B becomes oppoent A, and B is randomly chosen and displayed
# ask user again who has more followers