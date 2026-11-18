# Rock, Paper, Scissors Game using python progrsmming language

import random

choices = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors!")

user = input("Choose rock, paper, or scissors: ").lower()

computer = random.choice(choices)

print("\nYour Choice:", user)
print("Computer Choice:", computer)

if user not in choices:
    print("Invalid choice!")

elif user == computer:
    print("It's a Tie!")

elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("Congratulations! You Win!")

else:
    print("Computer Wins!")
