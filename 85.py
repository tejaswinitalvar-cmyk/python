# Find the first number divisible by 7 using python programming language 

numbers = [10, 15, 22, 25, 35, 42]

for num in numbers:
    if num % 7 == 0:
        print("First number divisible by 7 =", num)
        break
