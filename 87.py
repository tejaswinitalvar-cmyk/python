# Find the first number divisible by 4 using python programming language 

numbers = [7, 13, 19, 24, 32, 40]

for num in numbers:
    if num % 4 == 0:
        print("First number divisible by 4 =", num)
        break
