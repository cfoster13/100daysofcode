# Work out a list of prime factors
# 21 : [3, 7]

def prime_factor(n):
    prime_factors = []
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            prime_factors.append(divisor)
            n = n / divisor
        else:
            divisor += 1
    
    print(prime_factors)
    print(f"The largest prime is: {[prime_factors[-1]]}")
        
prime_factor(600851475143)

# Print out the largest 


    


