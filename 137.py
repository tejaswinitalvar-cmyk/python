# Count numbers with unique digits using python programming language 

numbers = [123, 112, 456, 787, 908, 555]
count = 0

for num in numbers:
    digits = str(num)

    if len(digits) == len(set(digits)):
        count += 1

print("Numbers with unique digits =", count)
