
import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock",  "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}


def check_win(player, computer):
    print(f"You chose {player}. Computer chose {computer}.")


    #scenario 1
    if player == computer:
        return "Its a tie!"


    #scenario 2
    elif player == "rock":
        if computer == "scissors" :
            return "Rock smashes scissors, you win!"
        else:
            return "Paper covers rock, you lose..."


    #scenario 3
    elif player == "paper":
        if computer == "rock" :
            return "Paper covers rock. You win!"
        else:
         return "Scissors cut Paper! You lose...!"

    #scenario 4
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper. You win"

        else:
            return "Rock beats scissors. You lose."


check_win("rock", "paper")
