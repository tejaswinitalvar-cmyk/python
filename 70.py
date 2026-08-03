# Find the sum of odd numbers in a list using python programming language 

numbers = [10, 15, 20, 25, 30, 35]

total = 0

for num in numbers:
    if num % 2 != 0:
        total += num

print("Sum of odd numbers =", total)
