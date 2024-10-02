print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? £"))
tip_amount = int(input("What percentage tip would you like to give? 10, 12, or 15: "))
amount_of_people = int(input("How many people to split the bill? "))

tip_amount_percentage = (tip_amount / 100) * total_bill # Converting tip from percentage to decimal then multiplying to find tip percentage of the bill
total_bill += tip_amount_percentage # updating the total bill with the tip added onto
amount_to_pay = float(total_bill / amount_of_people)
final_amount = round(amount_to_pay, 2) # Round to two decimal places

print(f"Final bill total is: £{final_amount}")

# 100, 10% tip

# 70, 10%