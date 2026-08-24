# Find the first number divisible by 11 using python programming language

numbers = [10, 23, 35, 44, 55, 66]

for num in numbers:
    if num % 11 == 0:
        print("First number divisible by 11 =", num)
        break
