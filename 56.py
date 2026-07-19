# Count words ending with a vowel using python programming language 

sentence = input("Enter a sentence: ")

words = sentence.split()

count = 0

for word in words:
    if word[-1].lower() in "aeiou":
        count += 1

print("Words ending with a vowel =", count)
