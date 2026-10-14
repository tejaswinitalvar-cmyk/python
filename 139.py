# Count numbers with descending digits using python programming language 

numbers = [321, 987, 654, 123, 950, 777]
count = 0

for num in numbers:
    digits = str(num)

    if all(digits[i] >= digits[i + 1]
           for i in range(len(digits) - 1)):
        count += 1

print("Numbers with descending digits =", count)
