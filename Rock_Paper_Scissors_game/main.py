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
if player_input == "ROCK" or player_input == "Rock" or player_input == "rock":
    player_input = "ROCK"
if player_input == "PAPER" or player_input == "Paper" or player_input == "paper":
    player_input = "PAPER" 
if player_input == "SCISSORS" or player_input == "Scissors" or player_input == "scissors":
    player_input = "SCISSORS"

for i in list_of_possible_choice:
    print (i) 
    print (i[0])
    print (i[1])
    print (i[2])
    if player_input != i:
        print("The option you chose is invalid, try again")
    
print(list_of_possible_choice[0])
