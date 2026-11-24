# Text File Analyzer using python programming language 

filename = "sample.txt"

with open(filename, "r") as file:
    content = file.read()

words = content.split()
characters = len(content)
lines = content.splitlines()

print("--- Text File Analysis ---")
print("Total Words:", len(words))
print("Total Characters:", characters)
print("Total Lines:", len(lines))
