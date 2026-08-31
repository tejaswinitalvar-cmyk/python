# Find the last even number in a list using python programming language 

numbers = [15, 22, 31, 40, 27, 18]

for num in reversed(numbers):
    if num % 2 == 0:
        print("Last even number =", num)
        break
