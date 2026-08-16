# Find the first odd number in a list using python programming language 

numbers = [12, 24, 18, 35, 40, 51]

for num in numbers:
    if num % 2 != 0:
        print("First odd number =", num)
        break
