# Find the smallest number that can evenly be divided from 1 to 20 without a remainder

""" smallest_number = 20
number_found = False




def find_smallest_n(i):
    for i in range(1, 11):
        if smallest_number % i == 0:
            i += 1
            print(f"smallest number {i}")
        else:
            return 

find_smallest_n(2520) """

# while loop to go through each number continues if number up to 20 isn't found




# 2520: 2520 / 1, 2520 / 2, 2520 / 3, up until 10 no remainder
# 450 / 3 has a remainder
# smallest multiple = count up from one until you reach 10 = while loop

def is_divisable(number):
    for i in range(2, 21):
        if number % i != 0:
            return False
    
    return True

number = 2

while True:
    if is_divisable(number):
        print(f"The smallest multiple is: {number}")
        break
    number += 2


