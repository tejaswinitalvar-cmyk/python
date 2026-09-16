# Check whether a number is a Spy Number using python programming language 

num = int(input("Enter a number: "))

temp = num
digit_sum = 0
digit_product = 1

while temp > 0:
    digit = temp % 10
    digit_sum += digit
    digit_product *= digit
    temp //= 10

if digit_sum == digit_product:
    print("It is a Spy Number.")
else:
    print("It is not a Spy Number.")
