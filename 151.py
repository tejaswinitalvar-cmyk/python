# Word Length Analyzer using python programming language 

sentence = input("Enter a sentence: ")

words = sentence.split()

for word in words:
    print(word, "=", len(word), "characters")

if words:
    longest = max(words, key=len)
    shortest = min(words, key=len)

    print("Longest word:", longest)
    print("Shortest word:", shortest)
else:
    print("No words entered.")
  
