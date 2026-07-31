# Count positive, negative, and zero values using python programming language 

numbers = [10, -5, 0, 25, -8, 0, 7]

positive = 0
negative = 0
zero = 0

for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print("Positive =", positive)
print("Negative =", negative)
print("Zero =", zero)
