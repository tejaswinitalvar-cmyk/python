# Find missing numbers in a range using python programming language 

numbers = [1, 2, 4, 6, 7, 9]

missing = []

for i in range(1, 10):
    if i not in numbers:
        missing.append(i)

print("Missing numbers:", missing)
