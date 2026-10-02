# Find the sum of digits at even positions using python programming language

num = input("Enter a number: ")

total = 0

for i in range(1, len(num), 2):
    total += int(num[i])

print("Sum of digits at even positions =", total)
