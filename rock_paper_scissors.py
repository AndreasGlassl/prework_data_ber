import random
# Import the choice function of the random module
# https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list

# Assign to a list the 3 possible options: 'rock', 'paper' or 'scissors'.

options = ['rock','paper','scissors']

# Assign a variable to the maximum number of games: 1, 3, 5, etc ...

print("How many games should be played in total?")
number_of_games = int(input())

# depending on number of games, this would make sure its an odd number
# number_of_games = int(input())*2-1


# Assign a variable to the number of games a player must win to win.
# Preferably the value will be based on the number of maximum games

number_of_wins = ((number_of_games)+1)/2

# Define a function that randomly returns one of the 3 options.
# This will correspond to the play of the machine. Totally random.

def select_random(x):
    outcome = random.choice(x)
    return outcome


# Define a function that asks your choice: 'stone', 'paper' or 'scissors'
# you should only allow one of the 3 options. This is defensive programming.
# If it is not stone, paper or scissors keep asking until it is.

def select_choice():
    while True:
        try:
            choice = str(input("Please choose your weapon, master!"))
        except ValueError:
            print("Please try again, master!")
            return select_choice()
        if (choice!="rock") & (choice!="paper") & (choice!="scissor"):
            print("Please choose your weapon, master! Hint: It is either rock, paper or scissors")
            return select_choice()
        else:
            return choice
        
player1 = select_choice()


# Define a function that resolves a combat.
# Returns 0 if there is a tie, 1 if the machine wins, 2 if the human player wins

    
# Define a function that shows the choice of each player and the state of the game
# This function should be used every time accumulated points are updated

    
# Create two variables that accumulate the wins of each participant


# Create a loop that iterates while no player reaches the minimum of wins
# necessary to win. Inside the loop solves the play of the
# machine and ask the player's. Compare them and update the value of the variables
# that accumulate the wins of each participant.


    
# Print by console the winner of the game based on who has more accumulated wins
  