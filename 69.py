# Find the average of even numbers in a list using python programming language 

numbers = [10, 15, 20, 25, 30, 35]

total = 0
count = 0

for num in numbers:
    if num % 2 == 0:
        total += num
        count += 1

average = total / count

print("Average of even numbers =", average)
