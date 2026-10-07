# Find the number with the lowest digit sum using python programming language 

numbers = [123, 45, 678, 91]

lowest_number = numbers[0]
lowest_sum = sum(int(digit) for digit in str(numbers[0]))

for num in numbers:
    digit_sum = sum(int(digit) for digit in str(num))

    if digit_sum < lowest_sum:
        lowest_sum = digit_sum
        lowest_number = num

print("Number with lowest digit sum =", lowest_number)
print("Lowest digit sum =", lowest_sum)
