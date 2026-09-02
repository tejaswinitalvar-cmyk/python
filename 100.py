# Simple number guessing game using python programming language 

secret = 7

guess = int(input("Guess the number (1-10): "))

if guess == secret:
    print("Congratulations! You guessed it!")
elif guess < secret:
    print("Too low!")
else:
    print("Too high!")
