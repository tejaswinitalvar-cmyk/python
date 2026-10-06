# Find the number with the highest digit sum using python programming language 

numbers = [123, 45, 678, 91]

highest_number = numbers[0]
highest_sum = 0

for num in numbers:
    temp = num
    digit_sum = 0

    while temp > 0:
        digit_sum += temp % 10
        temp //= 10

    if digit_sum > highest_sum:
        highest_sum = digit_sum
        highest_number = num

print("Number with highest digit sum =", highest_number)
print("Highest digit sum =", highest_sum)
