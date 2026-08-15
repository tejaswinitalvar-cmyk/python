# Find the first even number in a list using python programming language 

numbers = [15, 27, 33, 18, 25, 40]

for num in numbers:
    if num % 2 == 0:
        print("First even number =", num)
        break
