# Check whether a list contains only even numbers using python programming language 

numbers = [2, 4, 6, 8, 10]

all_even = True

for num in numbers:
    if num % 2 != 0:
        all_even = False
        break

if all_even:
    print("The list contains only even numbers.")
else:
    print("The list does not contain only even numbers.")
