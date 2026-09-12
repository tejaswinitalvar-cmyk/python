# Check whether a number is a Perfect Number using python programming language 

num = int(input("Enter a number: "))

total = 0

for i in range(1, num):
    if num % i == 0:
        total += i

if total == num:
    print("It is a Perfect Number.")
else:
    print("It is not a Perfect Number.")
