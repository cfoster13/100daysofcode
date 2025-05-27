# Reads the same way forward to back
# Largest palindrome made from a product of two 3 digit numbers
# 100 - 999

# -----------------

# Loop through every 3 digit number
# Muliply two 3 digit numbers together
# Check whether it's a palindrome
# If true largest palindrome becomes that, then repeat

#start by multiplying a = 999, by b = 999, then decrease b by 1: 999 x 998, 999 x 987, 999 x 986, 999 x 985 when b becomes 100
# decrease a by 1: 998 x 998, 998 x 997

largest_palindrome = 0

def palindrome(n):
    n_str = str(n)
    if n_str == n_str[::-1]: # if number reads the same forward as backwards
        return True
    else:
        return False
    
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if palindrome(product) and product > largest_palindrome:
            largest_palindrome = product

print(f"The largest palindrome made from a product is: {largest_palindrome}")


    

