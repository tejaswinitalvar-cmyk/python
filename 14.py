# Count vowels in a string using python programming language 

text = input("Enter a string: ")

count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Number of vowels:", count)
