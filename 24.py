# Count spaces in a string using python programming language 

text = input("Enter a sentence: ")

spaces = 0

for ch in text:
    if ch == " ":
        spaces += 1

print("Number of spaces =", spaces)
