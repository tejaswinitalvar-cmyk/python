# Check whether a number is a Neon Number using python programming language 

num = int(input("Enter a number: "))

square = num * num
digit_sum = 0

while square > 0:
    digit_sum += square % 10
    square //= 10

if digit_sum == num:
    print("It is a Neon Number.")
else:
    print("It is not a Neon Number.")
