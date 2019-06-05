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

computer_choice = random.choice(["rock","paper","scissors"])
print("------------")
print("GENERATING...")
print("COMPUTER CHOSE:",computer_choice)

# DETERMINE THE WINNER



# DISPLAY FINAL OUTPUTS / OUTCOMES