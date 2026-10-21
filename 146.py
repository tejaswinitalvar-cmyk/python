# Find the number with the most digits divisible by 3 using python programming language 

numbers = [1236, 4569, 7812, 3335, 9024]

max_count = -1
result = None

for num in numbers:
    count = 0

    for digit in str(abs(num)):
        if int(digit) % 3 == 0:
            count += 1

    if count > max_count:
        max_count = count
        result = num

print("Number with the most digits divisible by 3 =", result)
print("Count =", max_count)
