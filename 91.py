# Find the first number divisible by 10 using python programming language 

numbers = [13, 27, 35, 42, 50, 60]

for num in numbers:
    if num % 10 == 0:
        print("First number divisible by 10 =", num)
        break
