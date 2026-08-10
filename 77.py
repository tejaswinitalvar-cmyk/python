# Finding the sum of numbers at odd positions using python programming language

numbers = [10, 20, 30, 40, 50, 60]

total = 0

for i in range(1, len(numbers), 2):
    total += numbers[i]

print("Sum of numbers at odd positions =", total)
