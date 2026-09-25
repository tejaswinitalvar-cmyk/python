# Check whether a number is a Kaprekar Number using python programming language

num = int(input("Enter a number: "))

square = num * num
digits = len(str(num))

right = square % (10 ** digits)
left = square // (10 ** digits)

if left + right == num:
    print("It is a Kaprekar Number.")
else:
    print("It is not a Kaprekar Number.")
