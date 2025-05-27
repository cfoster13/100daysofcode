# Find the sum of squares: 1^2, 2^2 up to 10 = 385
# Loop through each number up to n ** 2
# add each number up to n, then ** 2
# minus the difference



def sum_of_squares(number):
    sum = 0
    for i in range(1, number + 1):
        square = i**2
        sum += square

    return sum

def square_of_sum(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i

    return sum ** 2

num_one = sum_of_squares(100)
num_two = square_of_sum(100)
difference = num_two - num_one

print(f"The difference between the sum of squares and square of the sum is {difference}")