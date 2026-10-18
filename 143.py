# Find the number with the smallest digit sum using python programming language 

numbers = [123, 451, 222, 105, 34]

smallest_sum = float("inf")
result = None

for num in numbers:
    digit_sum = sum(int(digit) for digit in str(abs(num)))

    if digit_sum < smallest_sum:
        smallest_sum = digit_sum
        result = num

print("Number with the smallest digit sum =", result)
print("Smallest digit sum =", smallest_sum)
