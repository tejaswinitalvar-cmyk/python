# Find common characters between two strings using python programming language 

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

common = ""

for ch in string1:
    if ch in string2 and ch not in common:
        common += ch

print("Common characters:", common)
