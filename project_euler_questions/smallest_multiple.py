# Find the smallest number that can evenly be divided from 1 to 20 without a remainder
# while loop to go through each number continues if number up to 20 isn't found
# 2520: 2520 / 1, 2520 / 2, 2520 / 3, up until 10 no remainder
# 450 / 3 has a remainder
# smallest multiple = count up from one until you reach 10 = while loop

def is_divisable(number):
    for i in range(2, 21): # Check up to 20
        if number % i != 0: # Check if number has a remainder
            return False # not evenly divisable if there is a remainder
    
    return True

number = 2

while True:
    if is_divisable(number):
        print(f"The smallest multiple is: {number}")
        break
    number += 2 # Only even numbers are divisable

