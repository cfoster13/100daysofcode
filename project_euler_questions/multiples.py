# Find the sum of all the multiples of 3 or 5 below 1000

multiple_three = 3
multiple_five = 5
sum = 0

for i in range(1, 1000):
    if i % multiple_three == 0 or i % multiple_five == 0:
        sum += i

print(f"The sum is {sum}")
