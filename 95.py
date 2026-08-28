# Find the first number divisible by 15 using python programming language 

numbers = [10, 22, 28, 45, 50, 60]

for num in numbers:
    if num % 15 == 0:
        print("First number divisible by 15 =", num)
        break
