# Finding the sum of numbers divisible by 3 using python programming language

numbers = [9, 10, 12, 15, 20, 21, 25]

total = 0

for num in numbers:
    if num % 3 == 0:
        total += num

print("Sum of numbers divisible by 3 =", total)
