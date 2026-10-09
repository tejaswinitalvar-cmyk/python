# Check whether two numbers have the same digit sum using python programming language 

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum1 = sum(int(digit) for digit in str(abs(num1)))
sum2 = sum(int(digit) for digit in str(abs(num2)))

print("First digit sum =", sum1)
print("Second digit sum =", sum2)

if sum1 == sum2:
    print("Both numbers have the same digit sum.")
else:
    print("Both numbers have different digit sums.")
