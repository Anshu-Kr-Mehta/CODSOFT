# rock_paper_scissors.py

import random

print("Welcome to Rock-Paper-Scissors Game!")

choices = ["rock", "paper", "scissors"]

user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
computer_choice = random.choice(choices)

print("You chose:", user_choice)
print("Computer chose:", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "scissors" and computer_choice == "paper") or \
     (user_choice == "paper" and computer_choice == "rock"):
    print("You win!")
elif user_choice in choices:
    print("You lose!")
else:
    print("Invalid input. Please choose rock, paper, or scissors.")
