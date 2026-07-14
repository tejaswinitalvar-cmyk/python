# Count the frequency of each word in a sentence using python programming language 

sentence = input("Enter a sentence: ").lower()

words = sentence.split()

for word in set(words):
    print(word, "=", words.count(word))
