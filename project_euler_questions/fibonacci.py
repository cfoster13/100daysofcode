# Add the previous two terms
# Find the sum of the even valued terms

term_one = 0
term_two = 1
even_nums = 0

while term_two < 4000000:
    
    if term_two % 2 == 0:
        even_nums += term_two

    next_term = term_one + term_two # calculate the next term 
    term_one = term_two
    term_two = next_term # Shifting the numbers along


print(even_nums)



    


