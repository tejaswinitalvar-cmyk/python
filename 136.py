# Count numbers that contain repeated digits using python programming language 

numbers = [112, 123, 455, 678, 900, 345]

count = 0

for num in numbers:
    digits = str(num)

    if len(digits) != len(set(digits)):
        count += 1

print("Numbers with repeated digits =", count)
