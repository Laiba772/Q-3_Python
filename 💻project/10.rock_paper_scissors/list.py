# project 4.  Rock, Paper,Scissors Game.

import random

# game choices.

print("Welcome to the Rock, Paper, Scissors Game!")

# list of possible choices.
choices = ['rock', 'paper', 'scissors']

# player choices.

player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

# computer's choice.

computer_choice = random.choice(choices)

# winner decision.

if player_choice == computer_choice:

    print(f"It's a tie! Both {player_choice}s.")

elif player_choice == 'rock' and computer_choice == 'scissors':
    print(f"Player wins! {player_choice} beats {computer_choice}")

elif player_choice == 'scissors' and computer_choice == 'paper':
    print(f"Player wins! {player_choice} beats {computer_choice}")

elif player_choice == 'paper' and computer_choice == 'rock':
    print(f"Player wins! {player_choice} beats {computer_choice}")

else:
    print(f"Computer wins! {computer_choice} beats {player_choice}")
