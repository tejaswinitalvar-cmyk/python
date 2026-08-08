# Finding the most frequent number in a list using programming language

numbers = [10, 20, 10, 30, 20, 10, 40]

most_frequent = max(set(numbers), key=numbers.count)

print("Most frequent number =", most_frequent)
