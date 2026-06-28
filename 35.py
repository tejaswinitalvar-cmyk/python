# Check whether two strings are anagrams using python programming language 

string1 = input("Enter first string: ").lower()
string2 = input("Enter second string: ").lower()

if sorted(string1) == sorted(string2):
    print("Anagram")
else:
    print("Not an anagram")
