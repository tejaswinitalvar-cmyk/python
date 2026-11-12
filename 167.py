# Typing Speed Test using python programming language 

import time

sentence = "Python is fun and easy to learn"

print("Welcome to Typing Speed Test!")
print("\nType this sentence:")
print(sentence)

input("\nPress Enter when you are ready...")

start_time = time.time()

typed_text = input("\nStart typing: ")

end_time = time.time()

time_taken = end_time - start_time

words = len(typed_text.split())
speed = (words / time_taken) * 60 if time_taken > 0 else 0

correct = 0

for i in range(min(len(sentence), len(typed_text))):
    if sentence[i] == typed_text[i]:
        correct += 1

accuracy = (correct / len(sentence)) * 100

print("\n--- Typing Test Results ---")
print("Time Taken:", round(time_taken, 2), "seconds")
print("Typing Speed:", round(speed, 2), "WPM")
print("Accuracy:", round(accuracy, 2), "%")
