# Check whether a number is a Harshad Number using python programming language 

num = int(input("Enter a number: "))

temp = num
digit_sum = 0

while temp > 0:
    digit_sum += temp % 10
    temp //= 10

if num % digit_sum == 0:
    print("It is a Harshad Number.")
else:
    print("It is not a Harshad Number.")
