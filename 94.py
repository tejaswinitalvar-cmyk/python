# Find the first number divisible by 13 using python programming language

numbers = [10, 25, 39, 45, 52, 65]

for num in numbers:
    if num % 13 == 0:
        print("First number divisible by 13 =", num)
        break
