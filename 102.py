# Reverse a list using a loop using python programming language 

numbers = [10, 20, 30, 40, 50]

reversed_list = []

for num in numbers:
    reversed_list.insert(0, num)

print("Original list:", numbers)
print("Reversed list:", reversed_list)
