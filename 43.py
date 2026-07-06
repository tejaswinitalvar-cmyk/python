# Find the largest word in a list using python programming language 

words = ["apple", "banana", "grapes", "watermelon", "kiwi"]

largest = words[0]

for word in words:
    if len(word) > len(largest):
        largest = word

print("Largest word:", largest)
