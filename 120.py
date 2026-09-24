# Check whether a number is a Pronic Number using python programming language 

num = int(input("Enter a number: "))

is_pronic = False

for i in range(1, num + 1):
    if i * (i + 1) == num:
        is_pronic = True
        break

if is_pronic:
    print("It is a Pronic Number.")
else:
    print("It is not a Pronic Number.")
