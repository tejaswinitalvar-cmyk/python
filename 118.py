# Check whether a number is a Palindromic Number using python programming language 

num = input("Enter a number: ")

if num == num[::-1]:
    print("It is a Palindromic Number.")
else:
    print("It is not a Palindromic Number.")
