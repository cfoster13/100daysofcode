# Prime number is one that can be divisable by only itself and one
# All primes are odd
# Primes don't have a square root

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1): # Check up to the square root 
        if num % i == 0: # Check if evenly divisable by nums up to square root
            return False
    return True
    

prime_count = 1
n = 2

while prime_count < 10001:
    n += 1
    if is_prime(n):
        prime_count += 1
print(n)