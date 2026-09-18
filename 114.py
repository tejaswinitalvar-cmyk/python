# Check whether a number is an Automorphic Number using python programming language 

num = int(input("Enter a number: "))

square = num * num

if str(square).endswith(str(num)):
    print("It is an Automorphic Number.")
else:
    print("It is not an Automorphic Number.")
