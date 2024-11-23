#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


letter_template = 'week5/Mail Merge Project Start/Input/Letters/starting_letter.txt'
names_path = 'week5/Mail Merge Project Start/Input/Names/invited_names.txt'
output_file_path = 'week5/Mail Merge Project Start/Output/ReadyToSend'

PLACEHOLDER = "[name]"


#Open the starting letter template
with open(letter_template, 'r') as template_file:
    template_text = template_file.read() # Read the entire file

# Read list of names
with open(names_path, 'r') as names_file:
    names = names_file.readlines() # Read all the names
    
    for name in names:
        stripped_name = name.strip()
        new_letter = template_text.replace(PLACEHOLDER, stripped_name)
        with open(f'week5/Mail Merge Project Start/Output/ReadyToSend/letter_for_{stripped_name}.docx', mode = "w") as completed_letter:
            completed_letter.write(new_letter)







