# Check whether a number is a Strong Number using python programming language 

import math

num = int(input("Enter a number: "))

total = 0
temp = num

while temp > 0:
    digit = temp % 10
    total += math.factorial(digit)
    temp //= 10

if total == num:
    print("It is a Strong Number.")
else:
    print("It is not a Strong Number.")
