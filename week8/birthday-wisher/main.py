##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import pandas as pd
import datetime as dt
import random
import smtplib

my_email = "xerneas01best@gmail.com"
gmail_pass = "fyanbhodjvgweohg"

#Read csv
data = pd.read_csv("week8/birthday-wisher/birthdays.csv")

# Convert dataframe to list of dicts
birthday_dict = data.to_dict(orient='records')

#Get current day and month
now = dt.datetime.now()
current_day = now.weekday()
current_month = now.date().month

print(current_day)
print(current_month)

# Paths to letters
letter_templates = [
    "week8/birthday-wisher/letter_templates/letter_1.txt",
    "week8/birthday-wisher/letter_templates/letter_2.txt",
    "week8/birthday-wisher/letter_templates/letter_3.txt",

]

PLACEHOLDER = "[NAME]"

for entry in birthday_dict:
    if entry["day"] == current_day and entry["month"]:
        name = entry["name"]
        # Choose a random letter template
        rand_letter = random.choice(letter_templates)
        # Read and customise the file
        with open(rand_letter, 'r') as letter_file:
            letter_text = letter_file.read()
            customised_letter = letter_text.replace(PLACEHOLDER, name)
        with open(f"week8/birthday-wisher/output_letter_for_{name}.txt", "w") as output_file:
            output_file.write(customised_letter)
            print(f"Customised birthday message made for {name}")


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=gmail_pass)
    if customised_letter:
        connection.sendmail(from_addr=my_email, to_addrs="xerneas01@yahoo.com", msg=f"Subject:Birthday Wish\n\n{customised_letter}")
        print("sending email...")
        



