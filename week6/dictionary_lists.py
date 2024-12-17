import random

numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
name = "Angela"
letters_list = [letter for letter in name]

print(new_numbers)
print(letters_list)

# Create a new list from a range where each number is doubled

 
doubled_numbers = [n * 2 for n in range(1, 5)]

print(doubled_numbers)

names = ["Alex", "Beth", "Sam", "Freddie"]

# Only print out short names when the length is less than 4
short_names = [name for name in names if len(name) < 4]

print(short_names)

# Print all names in capitals if length is longer than 5

capital_names = [name.upper() for name in names if len(name) > 5]

print(capital_names)


# Dictionary comprehension

# Generate a random score for each student
student_scores = {student:random.randint(1, 100) for student in names}

# Create a dictionary of students that have passed

passed_students = {student:score for (student, score) in student_scores.items() if score > 60}

print(student_scores.keys())
print(student_scores)
print(passed_students)

