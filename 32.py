# Find the longest word in a sentence using python programming language 

sentence = input("Enter a sentence: ")

words = sentence.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word =", longest)
