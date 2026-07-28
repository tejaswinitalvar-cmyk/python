# Count words longer than 5 characters using python programming language 

sentence = input("Enter a sentence: ")

words = sentence.split()

count = 0

for word in words:
    if len(word) > 5:
        count += 1

print("Words longer than 5 characters =", count)
