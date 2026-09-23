# Check whether a number is a Happy Number using python programming language 

num = int(input("Enter a number: "))

seen = set()

while num != 1 and num not in seen:
    seen.add(num)

    total = 0
    while num > 0:
        digit = num % 10
        total += digit * digit
        num //= 10

    num = total

if num == 1:
    print("It is a Happy Number.")
else:
    print("It is not a Happy Number.")
