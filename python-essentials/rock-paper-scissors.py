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