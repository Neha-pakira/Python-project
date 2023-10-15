#rock paper scissors game
'''rock vs paper=paper wins
paper vs scissors=scissors wins
rock vs scissors=rock wins'''
import random

# Getting users choice
user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

# Generating a random choice
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)

# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("You win!")
    else:
        print("Computer wins!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You win!")
    else:
        print("Computer wins!")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("You win!")
    else:
        print("Computer wins!")
else:
    print("Invalid choice. Please choose rock, paper, or scissors.")
