# Find the sum of positive numbers in a list using python programming language

numbers = [10, -5, 20, -8, 15, 0]

total = 0

for num in numbers:
    if num > 0:
        total += num

print("Sum of positive numbers =", total)
