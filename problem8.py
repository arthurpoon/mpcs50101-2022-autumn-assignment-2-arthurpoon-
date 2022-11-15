#Arthur Poon
#MPCS 50101 2,1 Intro to Programming Monday Section
#Problem 8

import random

# Randomly select an object for the computer's choice   
def play_rps():
    computer_object = random.choice(["paper","rock","scissors"])

#take input from user
    input_choice = input("Choose: ")

#check if valid input
    if input_choice not in ["rock", "paper", "scissors"]:
        print("You must choose paper, rock or scissors.")
        play_rps()

#see who wins:
#if tie
    if computer_object == input_choice:
        print(f"Computer choose {computer_object}. Let's settle this.")
        play_rps()

#if not tie
    else:
        if computer_object == "rock" and input_choice == "paper":
            print(f"Computer choose {computer_object}, you win!")
        elif computer_object == "paper" and input_choice == "scissors": 
            print(f"Computer choose {computer_object}, you win!")
        elif computer_object == "scissors" and input_choice == "rock": 
            print(f"Computer choose {computer_object}, you win!")
        else:
            print(f"Computer choose {computer_object}, you lose!")

#ask user if they want to play again
    play_again = input("Would you like to play again? ")
    if play_again not in ["y","n"]:
        print("that is not a valid answer")
        play_again = input("Would you like to play again? ")
    else:
        pass
    if play_again == "y":
        play_rps()
    elif play_again == "n":
        exit()

play_rps()
