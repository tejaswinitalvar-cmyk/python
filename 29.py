# Count even and odd numbers in a list using python programming language 

numbers = [10, 15, 22, 33, 40, 51]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers =", even_count)
print("Odd numbers =", odd_count)
