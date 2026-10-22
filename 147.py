# Find the number with the most digits divisible by 5 using python programming language 

numbers = [1250, 5552, 3455, 9081, 5055]

max_count = -1
result = None

for num in numbers:
    count = 0

    for digit in str(abs(num)):
        if int(digit) % 5 == 0:
            count += 1

    if count > max_count:
        max_count = count
        result = num

print("Number with the most digits divisible by 5 =", result)
print("Count =", max_count)
