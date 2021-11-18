# Period 3
# Date Created: September 20th, 2021
# Name: Ahsan Shamim
# Description: Text-Based Adventure Game Menu

import sys


print("Text-Based Adventure Game")
print("Welcome User_")
# valid directions and actions for the characters
valid_actions = ["actions", "directions"]
possible_directions = ["Africa", "America", "Asia", "Antarctica"]
possible_actions = ["continue", "retreat", "teleport", "walk", "quit"]
# print a list a valid actions before user input. Organized according to
# valid actions
while True:
    print("How would you like to proceed?")
    for action in possible_actions:
        print(f"* {action}")
    # after user input, print out the action choosen by the user
    action_input = input("Action: ")
    if action_input.lower() in possible_actions:
        if action_input.lower() == "continue":
            for direction in possible_directions:
                print(f"* {direction}")
            direction_input = input("Which direction do you want to go? ")
            if direction_input.lower() in possible_directions:
                print(f"Go {direction_input}!")
            else:
                print("Africa!")
                
        elif action_input.lower() == "quit":
            print("Goodbye!")
            sys.exit()
        elif action_input.lower() in possible_actions:
            print(f"{action_input.title()}!")

        else:
            print("Invalid action!")