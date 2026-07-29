# Find the largest even number in a list using python programming language 

numbers = [15, 22, 9, 48, 31, 40]

largest = -1

for num in numbers:
    if num % 2 == 0 and num > largest:
        largest = num

print("Largest even number =", largest)
