# Who has read the most amount of books?

student_books = {
    "Alice": 4,
    "Bob": 7,
    "Charlie": 6,
    "Diana": 5,
}

total_books = 0
top_student = "" # set to a string

for books in student_books:
    if student_books[books] > total_books:
        total_books = student_books[books]
        top_student = books 

print(f"The highest number of books is: {total_books} read by {top_student}")

sales = { # Print the person with the least amount of sales
    "John": 500,
    "Sara": 300,
    "Lily": 700,
    "Paul": 400,
}



min_sales_person = ""
min_sales = float('inf') # any value smaller than infinity

for employees in sales:
    if sales[employees] < min_sales:
        min_sales = sales[employees]
        min_sales_person = employees

print(f"{min_sales} min sales made by {min_sales_person}")
