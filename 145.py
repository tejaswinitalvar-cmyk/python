# Find the number with the smallest product of digits using python programming language 

numbers = [123, 234, 105, 326, 412]

smallest_product = float("inf")
result = None

for num in numbers:
    product = 1

    for digit in str(abs(num)):
        product *= int(digit)

    if product < smallest_product:
        smallest_product = product
        result = num

print("Number with the smallest digit product =", result)
print("Smallest digit product =", smallest_product)
