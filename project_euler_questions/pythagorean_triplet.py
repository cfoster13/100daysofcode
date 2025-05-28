# a^2 + b^2 = c^2 - pythagorean triplet
# 3^2 + 4^2 = 25, square root is 5

# a + b + c = 1000
# c = 1000 - a - b

def find_triplet():
    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            c = 1000 - a - b 
            if a * a + b * b == c * c:
                print(f"The product of {a}, {b} and {c} is {a * b * c}")
                break

find_triplet()