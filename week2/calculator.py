
def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

def power(n1, n2):
    return n1**n2

calc_dict = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
    "^": power,
}
# Use the dict operations to perform a multiplication calculation e.g. 4 * 8

# Testing the calculator operations: print(calc_dict["*"](4, 8))

operation = ""

continue_calculating = True

def print_operations():
    for keys in calc_dict: # printing out the list of operations
        operation = keys
        print(keys)

def run_calculator():
    continue_calculating = True
    first_number = int(input("Enter your first number: "))

    while continue_calculating:
        print_operations()
        
        operation_choice = input("Choose an opeartion: ")
        second_number = int(input("Enter your second number: "))
        result = calc_dict[operation_choice](first_number, second_number)
        
        print(f"The result is {result}")
        continue_calculation = input("Would you like to continue calculating? y/n ").lower()

        if continue_calculation == "y":
            first_number = result # storing the first number from the previous result

        elif continue_calculation == "n":
            #Call the prompt for first number
            continue_calculating = False
            start_again = input("Would you like to start a new calculation? y/n ").lower()
            if start_again == "y":
                run_calculator()
            elif start_again == "n":
                print("Calculator session ended.")
    


run_calculator()



