# Find elements present in the first list but not in the second list

list1 = [10, 20, 30, 40, 50]
list2 = [20, 40, 60]

difference = []

for item in list1:
    if item not in list2:
        difference.append(item)

print("Difference:", difference)
