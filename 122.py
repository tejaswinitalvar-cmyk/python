# Check whether a number is a Fascinating Number using python programming language

num = int(input("Enter a number: "))

result = str(num) + str(num * 2) + str(num * 3)

if len(result) == 9 and set(result) == set("123456789"):
    print("It is a Fascinating Number.")
else:
    print("It is not a Fascinating Number.")
