# Find the length of each word using python programming language 

sentence = input("Enter a sentence: ")

words = sentence.split()

for word in words:
    print(word, "=", len(word))
