# Find the index of an element in a list using python programming language 

numbers = [10, 20, 30, 40, 50]

element = int(input("Enter the element to find: "))

if element in numbers:
    print("Index =", numbers.index(element))
else:
    print("Element not found.")
