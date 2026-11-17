# Number Guessing Game using python programming language 

import random

secret_number = random.randint(1, 20)
attempts = 0

print("Welcome to Number Guessing Game!")
print("Guess a number between 1 and 20.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("\nCongratulations! You guessed it!")
        print("Correct Number:", secret_number)
        print("Total Attempts:", attempts)
        break
      
