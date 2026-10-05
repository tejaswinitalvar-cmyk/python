# Find the sum of digits of all numbers in a list using python programming language 

numbers = [12, 25, 34, 41]

total = 0

for num in numbers:
    while num > 0:
        total += num % 10
        num //= 10

print("Sum of all digits =", total)
