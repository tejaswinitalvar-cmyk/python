# Find the number with the most odd digits using python programming language 

numbers = [1234, 1357, 4826, 97531, 8062]
max_count = -1
result = None

for num in numbers:
    count = 0

    for digit in str(abs(num)):
        if int(digit) % 2 != 0:
            count += 1

    if count > max_count:
        max_count = count
        result = num

print("Number with the most odd digits =", result)
print("Number of odd digits =", max_count)
