# Check whether all elements in a list are unique using python programming language 

numbers = [10, 20, 30, 40, 50]

if len(numbers) == len(set(numbers)):
    print("All elements are unique.")
else:
    print("The list contains duplicate elements.")
