# Count numbers divisible by 5 in a list using python programming language

numbers = [10, 13, 25, 18, 30, 42, 50]

count = 0

for num in numbers:
    if num % 5 == 0:
        count += 1

print("Numbers divisible by 5 =", count)
