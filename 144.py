# Find the number with the highest product of digits using python programming language 

numbers = [123, 234, 159, 326, 412]

highest_product = -1
result = None

for num in numbers:
    product = 1

    for digit in str(abs(num)):
        product *= int(digit)

    if product > highest_product:
        highest_product = product
        result = num

print("Number with the highest digit product =", result)
print("Highest digit product =", highest_product)
