import smtplib
import datetime as dt
import random

my_email = "xerneas01best@gmail.com"
gmail_pass = "fyanbhodjvgweohg"


now = dt.datetime.now()
day_of_week = now.weekday()
#print(day_of_week)

birthday = dt.datetime(year=2002, month=6, day=18)

# obtain the current day of the week
# open the quotes.txt file and obtain a list of quotes
# randomly select a quote from the list
# send an email to yourself

my_file = open("week8/Email/quotes.txt", "r")

data = my_file.read()

# replacing end splitting the text  
# when newline ('\n') is seen. 
data_into_list = data.split("\n")
rand_quote = random.choice(data_into_list)


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=gmail_pass)
    if day_of_week == 4:
        connection.sendmail(from_addr=my_email, to_addrs="xerneas01@yahoo.com", msg=f"Subject:Inspirational Quote\n\n{rand_quote}")
        print("sending email...")
        my_file.close() 