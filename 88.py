# Find the first number divisible by 6 using python programming language 

numbers = [7, 13, 25, 35, 42, 50]

for num in numbers:
    if num % 6 == 0:
        print("First number divisible by 6 =", num)
        break
