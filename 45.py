# Find the shortest word in a list using python programming language

words = ["apple", "banana", "cat", "watermelon", "kiwi"]

shortest = words[0]

for word in words:
    if len(word) < len(shortest):
        shortest = word

print("Shortest word:", shortest)
