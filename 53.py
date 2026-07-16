# Count special characters in a string using python programming language 

text = input("Enter a string: ")

count = 0

for ch in text:
    if not ch.isalnum() and ch != " ":
        count += 1

print("Number of special characters =", count)
