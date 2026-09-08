# Find the second smallest number in a list using python programming language 

numbers = [25, 10, 40, 5, 30, 15]

unique_numbers = list(set(numbers))
unique_numbers.sort()

print("Second smallest number =", unique_numbers[1])
