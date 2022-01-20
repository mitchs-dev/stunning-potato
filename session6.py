# Here are out imports
import random
import argparse
# Adds the '--rules' argument
parser = argparse.ArgumentParser()
parser.add_argument("-r", "--rules", dest="rules",
                    help="Prints the rules", action='store_true')
args = parser.parse_args()
# Checks if '--rules- or '-hr' was used
rulesSelected = bool(args.rules)

# Print rules if you type '--rules' or 'r'
if rulesSelected == True:
    print("######### RULES ########## \n" + "Here are the winning combinations for this game: \n"
          + "Rock vs Paper-> Paper wins \n"
          + "Rock vs Scissor-> Rock wins \n"
          + "Paper vs Scissor-> Scissor wins")
    quit()

# Determines if the 'while' loop should go again. This sets the default to '0'
goAgain = 0

# Sets 'user' wins to '0' by default
userWin = 0
# Sets 'computer' wins to '0' by default
compWin = 0

while True:
    print("Let's play!\n  Rock..\n    Paper..\n      Scissor..\n            SHOOT!")

    # initialize value of choice_name variable
    # corresponding to the choice value
    choice = random.randint(1, 3)
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'
# Prints the user choice
    print("user choice is: " + choice_name)
    # initialize value of comp_choice_name
    # variable corresponding to the choice value
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'

    print(choice_name + " V/s " + comp_choice_name)

 # Condition for winning
    if((choice == 1 and comp_choice == 2) or
       (choice == 2 and comp_choice == 1)):
        print("Paper wins!\n ", end="")
        result = "paper"

    elif((choice == 1 and comp_choice == 3) or
         (choice == 3 and comp_choice == 1)):
        print("Rock wins!\n", end="")
        result = "Rock"
    else:
        print("Scissor wins!\n", end="")
        result = "scissor"
# Printing either user or computer wins
    if result == choice_name:
        print("<== User wins this round")
        # If the 'user' wins, add +1
        userWin = userWin + 1
    else:
        print("Computer wins this round ==>")
        # If the computer wins, add +1
        compWin = compWin + 1
# if 'goAgain' is equal to '3' break
    if goAgain == 2:
        if userWin > compWin:
            print("##############\n" +
                  "THE USER HAS WON! :D\n" + "Final Score:\n" + "User:" + str(userWin) + "\nComputer: " + str(compWin) + "\n##############\n")
            break
        if userWin == compWin:
            print("##############\n" +
                  "IT'S A TIE! :O\n" + "Final Score:\n" + "User:" + str(userWin) + "\nComputer: " + str(compWin) + "\n##############\n")
            break
        else:
            print("##############\n" +
                  "THE USER HAS LOST! :(\n" + "Final Score:\n" + "User:" + str(userWin) + "\nComputer: " + str(compWin) + "\n##############\n")
            break
    else:
        # If 'goAgain' isn't equal to three, it will continue the loop
        goAgain = goAgain + 1

# after coming out of the while loop
# we print thanks for playing
print("Thanks for playing")
