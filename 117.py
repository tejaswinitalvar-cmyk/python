# Check whether a number is a Buzz Number using python programming language 

num = int(input("Enter a number: "))

if num % 7 == 0 or num % 10 == 7:
    print("It is a Buzz Number.")
else:
    print("It is not a Buzz Number.")
