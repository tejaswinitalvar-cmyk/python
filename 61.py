# Check whether a number is a perfect square using python programming language 

num = int(input("Enter a number: "))

root = int(num ** 0.5)

if root * root == num:
    print(num, "is a Perfect Square")
else:
    print(num, "is Not a Perfect Square")
