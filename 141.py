# Find the number with the most even digits

numbers = [1234, 2689, 4826, 1357, 8062]
max_count = -1
result = None

for num in numbers:
    count = 0

    for digit in str(abs(num)):
        if int(digit) % 2 == 0:
            count += 1

    if count > max_count:
        max_count = count
        result = num

print("Number with the most even digits =", result)
print("Number of even digits =", max_count)
