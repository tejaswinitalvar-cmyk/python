# Find the number with the most digits using python programming language 

numbers = [45, 1234, 789, 56, 12345, 678]

longest = numbers[0]

for num in numbers:
    if len(str(num)) > len(str(longest)):
        longest = num

print("Number with the most digits =", longest)
