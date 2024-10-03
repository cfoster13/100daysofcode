# Even numbers have a % of 0 when halfed e.g. 12 % 2 = 0

print("Welcome to Even or Odd")
num = int(input("Enter your number: "))

if num % 2 == 0:
    print("Your number is Even")
elif num % 2 != 0:
    print("Your number is Odd")
else:
    print("Not a valid input")