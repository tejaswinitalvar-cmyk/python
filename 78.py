# Find the sum of negative numbers in a list using python programming language

numbers = [10, -5, 20, -8, 15, -2]

total = 0

for num in numbers:
    if num < 0:
        total += num

print("Sum of negative numbers =", total)
