# Find the smallest odd number in a list using python programming language 

numbers = [12, 7, 25, 3, 18, 11]

smallest = None

for num in numbers:
    if num % 2 != 0:
        if smallest is None or num < smallest:
            smallest = num

print("Smallest odd number =", smallest)
