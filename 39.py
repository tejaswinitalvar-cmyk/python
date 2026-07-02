# Find common elements in two lists using python programming language 

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

intersection = []

for item in list1:
    if item in list2:
        intersection.append(item)

print("Intersection:", intersection)
