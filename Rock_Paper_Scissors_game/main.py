#Rock Paper Scissors game

import random
from secrets import choice

print("Welcome to this Rock Paper Scissors game")
list_of_possible_choice = ["ROCK", "PAPER", "SCISSORS"]
player_name = str(input("Enter your name PLAYER 1: "))
print(f"Welcome {player_name} so nice of you to join us for ROCK PAPER SCISSORS ")
player_input = input("Player One enter your pick e.g Rock, Paper or Scissors: ")
computer_choice = choice(list_of_possible_choice)
print("Player 1 chose "+ player_input)
print("CPU chose "+computer_choice)
print(f"computer {computer_choice} : player {player_input}")

option1 = list_of_possible_choice[0]
option2 = list_of_possible_choice[1]
option3 = list_of_possible_choice[2]


for i in list_of_possible_choice:
    print(i)
    
    #All the possible choice the player could Enter to reduce more errors.  
    if player_input == "ROCK" or player_input == "Rock" or player_input == "rock" or player_input == "R" or player_input == "r":
        player_input = "ROCK" 
        option1 == player_input
    if player_input == "PAPER" or player_input == "Paper" or player_input == "paper" or player_input =="P" or player_input == "p":
        player_input = "PAPER" 
        option2 == player_input
    if player_input == "SCISSORS" or player_input == "Scissors" or player_input == "scissors" or player_input == "S" or player_input =="s":
        player_input = "SCISSORS"
        option3 == player_input
    else: 
        print("The option you chose is invalid")
    # if player_input != option1 or player_input != option2 or player_input != option3:
    #         print("The option you chose isn't part of the possible options, Try Again" )
    i = newuser_input
    newuser_input = input("Enter your options again: ") 