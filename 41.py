# Merge two lists without duplicates using python programming language 

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

merged = list1.copy()

for item in list2:
    if item not in merged:
        merged.append(item)

print("Merged List:", merged)
