# Check whether a number is a Disarium Number using python programming language 

num = int(input("Enter a number: "))

digits = str(num)
total = 0

for i in range(len(digits)):
    total += int(digits[i]) ** (i + 1)

if total == num:
    print("It is a Disarium Number.")
else:
    print("It is not a Disarium Number.")
