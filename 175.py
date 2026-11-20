# Word Frequency Counter using python programming language

import string

sentence = input("Enter a sentence: ")

sentence = sentence.lower()

for char in string.punctuation:
    sentence = sentence.replace(char, "")

words = sentence.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\n--- Word Frequency Report ---")

for word, count in frequency.items():
    print(word, ":", count)
