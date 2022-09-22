
import random

def get_choices():

    
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock",  "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}

    return choices





def check_win(player, computer):
    #print("You choise " + player + "computer chose" + computer)
    # f string to do the same:
    print(f"You chose {player}. Computer chose {computer}.")


    if player == computer:
        
        
        
        
        
    

        
        return "Its a tie!"




age = 25
print(f"Jin is {age} years old.")






