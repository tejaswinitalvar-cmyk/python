# Find the number with the most prime digits using python programming language 

numbers = [2351, 7283, 4567, 9925, 1378]

max_count = -1
result = None

for num in numbers:
    count = 0

    for digit in str(abs(num)):
        if int(digit) in [2, 3, 5, 7]:
            count += 1

    if count > max_count:
        max_count = count
        result = num

print("Number with the most prime digits =", result)
print("Number of prime digits =", max_count)
