# Count positive and negative numbers in a list using python programming language 

numbers = [10, -5, 20, -8, 0, 15, -2]

positive = 0
negative = 0

for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1

print("Positive numbers =", positive)
print("Negative numbers =", negative)
