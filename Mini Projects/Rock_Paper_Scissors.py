import random

user_pick = 0
computer_pick = 0
computer_wins = 0
moves = ["rock", "paper", "scissors"]

while True:
    user_input = input("Rock, paper or scissors: ").lower()
    if user_input == "q":
        break
    if user_input == "rock":
        computer_pick = "paper"
    if user_input == "paper":
        computer_pick = "scissors"
    if user_input == "scissors":
        computer_pick = "rock"
    print("Computer chose", computer_pick)
    
