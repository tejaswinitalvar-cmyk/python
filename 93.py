# Find the first number divisible by 12 using python programming language 

numbers = [10, 25, 35, 48, 55, 60]

for num in numbers:
    if num % 12 == 0:
        print("First number divisible by 12 =", num)
        break
