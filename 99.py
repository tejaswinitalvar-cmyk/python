# Find the last odd number in a list using python programming language 

numbers = [12, 25, 30, 41, 50, 18]

for num in reversed(numbers):
    if num % 2 != 0:
        print("Last odd number =", num)
        break
