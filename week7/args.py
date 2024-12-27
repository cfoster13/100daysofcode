# Unlimited number of arguments


def add(*args):
    total = 0
    for n in args:
        total += n
    
    print(total)

add(5, 6, 4)