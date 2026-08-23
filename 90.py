# Find the first number divisible by 9 using python programming language 

numbers = [10, 17, 25, 36, 45, 54]

for num in numbers:
    if num % 9 == 0:
        print("First number divisible by 9 =", num)
        break
