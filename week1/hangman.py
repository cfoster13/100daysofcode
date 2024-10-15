import random
import hangman_words
import hangman_art

word_list = ["apple", "camel", "baboon"]
word_list_test = hangman_words.word_list

chosen_word = random.choice(word_list_test) # randomly select a word from the list

chosen_word_in_list = list(chosen_word) # Converting to a list to compare the letters

placeholder = ""
display = ""
n = 0
has_won = False


correct_letters = []
wrong_letters = []

print(hangman_art.logo)

for letters in chosen_word: 
    placeholder += "_"

lives = 6 # defining for hangman stages

while (has_won == False):
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Enter in a letter to guess: ").lower()
    display = "" # reset display to prevent duplicate underscores

    if guess in correct_letters or  guess in wrong_letters:
        print(f"You've already guessed {guess}. Try a different letter")
        continue # go onto the next thing
    
    wrong_guess = True

    for n in range(len(chosen_word)): # loop through the length of the chosen word length N times
        amount_of_repeated_guesses = 0
        if guess == chosen_word_in_list[n]: # if guess is in the word
            correct_letters.append(chosen_word_in_list[n]) # add the guess letter to the correct list
            wrong_guess = False # as player guessed correctly
            amount_of_repeated_guesses += 1
        if chosen_word_in_list[n] in correct_letters: # if a chosen word letter is in the correct letters list
            display += chosen_word_in_list[n] # readd it to the display (as this has been reset)
        


        else: #player gets the letter wrong
            display += "_"
            
         
    if wrong_guess:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            #print(stages[f])
            print(hangman_art.stages[lives])
            lives -= 1 # increment stage by one
            wrong_letters.append(guess) # store wrong letter in the list so it can be compared if user enters the same letter again
            wrong_guess = False # set back to false
            
            if lives == 0:
                print(f"It was {chosen_word}! You lose.")
                exit()  

    print(display)
    

    if "_" not in display:
        has_won = True
        print("Well done you won!")




# for i in range(len(chosen_word)): # Go through each letter of the guess to compare to the letters of chosen word
#     if guess == chosen_word_in_list[i]: 
#         print("Right")
#     else:
#         print("Wrong")




