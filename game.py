# game.py

import random #always include imports of modules at the start of a Python script. Prevents error of computer selection.

print("Rock, Paper, Scissors, Shoot!")

# CAPTURE INPUTS

user_choice = input("Please choose one of the following options: 'rock', 'paper', or 'scissors' (without the quotes)")
print("------------")
print("USER CHOSE:",user_choice)

# VALIDATE INPUTS

options = ["rock","paper","scissors"]

if user_choice in options: #in operator looks for a value or word in a list
    pass #or use print("VALID") to show VALID when rock, paper, scissors is correctly inputted.
else:
        print("INVALID SELECTION, PLEASE TRY AGAIN...")
        exit()

# GENERATE COMPUTER SELECTION

computer_choice = random.choice(options)
print("------------")
print("GENERATING...")
print("COMPUTER CHOSE:",computer_choice)

# DETERMINE THE WINNER
## rock beats scissors, paper beats rock, scissors beats paper, same selection is a tie

if user_choice == computer_choice:
    print("TIE")
elif user_choice == "rock" and computer_choice == "paper":
    print("PAPER")
elif user_choice == "rock" and computer_choice == "scissors":
    print("ROCK")
elif user_choice == "paper" and computer_choice == "rock":
    print("PAPER")
elif user_choice == "paper" and computer_choice == "scissors":
    print("SCISSORS")
elif user_choice == "scissors" and computer_choice == "rock":
    print("ROCK")
elif user_choice == "scissors" and computer_choice == "paper":
    print("SCISSORS")

# DISPLAY FINAL OUTPUTS / OUTCOMES