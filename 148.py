# Find the number with the most digits divisible by 7 using python programming language 

numbers = [1772, 7775, 1478, 9021, 7173]

max_count = -1
result = None

for num in numbers:
    count = 0

    for digit in str(abs(num)):
        if int(digit) % 7 == 0:
            count += 1

    if count > max_count:
        max_count = count
        result = num

print("Number with the most digits divisible by 7 =", result)
print("Count =", max_count)
