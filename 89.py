# Find the first number divisible by 8 using python programming language 

numbers = [7, 15, 22, 31, 40, 56]

for num in numbers:
    if num % 8 == 0:
        print("First number divisible by 8 =", num)
        break
