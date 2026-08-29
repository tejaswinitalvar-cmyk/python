# Find the first number greater than the average using python programming language 

numbers = [10, 20, 30, 40, 50]

average = sum(numbers) / len(numbers)

for num in numbers:
    if num > average:
        print("First number greater than average =", num)
        break
