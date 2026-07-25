# Count even and odd digits in a number using python programming language 

num = input("Enter a number: ")

even = 0
odd = 0

for digit in num:
    if int(digit) % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even digits =", even)
print("Odd digits =", odd)
