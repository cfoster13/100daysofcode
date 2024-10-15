alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(direction, original_text, shift_amount):
    if direction == "encode":
        new_word = ""

        for char in original_text: # loop through each letter in the plain text
            # find the position of each letter in the alphabet list and add it to the shift amount
            shifted_poisiton = alphabet.index(char) + shift_amount
            shifted_poisiton %= len(alphabet) # prevents index out of range, as it gets the remainder
            new_word += alphabet[shifted_poisiton] # add the new position to the empty string

        print(f"The encoded result is: {new_word}")

    elif direction == "decode":
        output_text = ""

        for char in original_text: # loop through each letter in the plain text
            # find the position of each letter in the alphabet list and add it to the shift amount
            shifted_poisiton = alphabet.index(char) - shift_amount # shift the letters backwards
            shifted_poisiton %= len(alphabet) # prevents index out of range, as it gets the remainder
            output_text += alphabet[shifted_poisiton] # add the new position to the empty string

        print(f"The decoded result is: {output_text}")

    else:
        print("Not a valid answer")




start_over = True

while start_over:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    answer = input("Type yes if you want to go again, or no to quit: ").lower()
    if answer == "yes":
        caesar(direction, text, shift)
    elif answer == "no":
        print("Exiting application...")
        start_over = False
        exit()







