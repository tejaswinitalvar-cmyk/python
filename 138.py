# Count numbers with ascending digits using python programming language 

numbers = [123, 145, 321, 246, 789, 112]
count = 0

for num in numbers:
    digits = str(num)

    if all(digits[i] <= digits[i + 1]
           for i in range(len(digits) - 1)):
        count += 1

print("Numbers with ascending digits =", count)
