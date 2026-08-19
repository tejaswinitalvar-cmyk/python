# Find the first number divisible by both 3 and 5 using python programming language 

numbers = [10, 18, 22, 30, 45, 60]

for num in numbers:
    if num % 3 == 0 and num % 5 == 0:
        print("First number divisible by 3 and 5 =", num)
        break
