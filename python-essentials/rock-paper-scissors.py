import random
"""we import this to enable the computer to choose its choices randomly"""

def get_choices():
    """this defines a function that gets choices"""

    player_choice = input("ENTER A CHOICE (rock, paper, scissors): ")
    """this promts the user to enter an input"""

    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    """this creates a lists of items then calls the comp to randomly choose from it"""

    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer):
    """function that checks who won"""

    print(f"You chose:{player}, Computer chose:{computer}")
    if player == computer:
        return ("Its a tie!")
    elif player == "rock":
        if computer == "scissors":
            return ("Rock smashes scissors! You win!")
        else:
            return ("Paper covers rock! You Lose.")
    elif player == "paper":
        if computer == "rock":
            return ("Paper covers rock! You win!")
        else:
            return ("Scissors cuts paper! You Lose.")
    elif player == "scissors":
        if computer == "paper":
            return ("Scissors cuts paper! You win!")
        else:
            return ("Rock smashes scissors! You Lose.")

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)