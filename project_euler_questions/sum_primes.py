# Find the sum of all primes below 2 million
# Keeping adding prime numbers to a list until the value reaches 2 million
# Remove the final value from the list

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1): # Check up to the square root 
        if num % i == 0: # Check if evenly divisable by nums up to square root
            return False
    return True

list_of_primes = []
n = 2
print("program running!...")

while n < 2000000:
    if is_prime(n): # If a prime number is found
        list_of_primes.append(n) # Add it to the list
    n += 1 # Increment


print(f"The sum of primes is: {sum(list_of_primes)}")