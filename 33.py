# Count the frequency of each character using python programming language 

text = input("Enter a string: ")

for ch in set(text):
    print(ch, "=", text.count(ch))
