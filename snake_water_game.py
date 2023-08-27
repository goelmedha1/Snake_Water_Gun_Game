# snake water game

import random

computer_score = 0
user_score = 0

i = 1
while i <= 10:
    print("Game no.:", i)

    game_var = ("snake", "water", "gun")
    choose = random.choice(game_var)
    # print(choose)

    user_input = input("Enter snake, water or gun to proceed \n")
    print("User entered ", user_input, "and Computer entered", choose)

    if choose == "snake" and user_input == "water":
        computer_score += 1
        print("Computer wins the game as snake drinks the water")
        print("Computer Scored: ", computer_score, "and User scored: ", user_score,"\n")
    elif choose == "snake" and user_input == "gun":
        user_score += 1
        print("User wins the game as gun kills the snake")
        print("Computer Scored: ", computer_score, "and User scored: ", user_score, "\n")
    elif choose == "water" and user_input == "gun":
        computer_score += 1
        print("Computer wins the game as gun drowns in water")
        print("Computer Scored: ", computer_score, "and User scored: ", user_score, "\n")
    elif choose == "water" and user_input == "snake":
        user_score += 1
        print("User wins as snake drinks the water")
        print("Computer Scored: ", computer_score, "and User scored: ", user_score, "\n")
    elif choose == "gun" and user_input == "snake":
        computer_score += 1
        print("Computer wins as gun kills the snake")
        print("Computer Scored: ", computer_score, "and User scored: ", user_score, "\n")
    elif choose == "gun" and user_input == "water":
        user_score += 1
        print("User wins the game as gun drowns in water")
        print("Computer Scored: ", computer_score, "and User scored: ", user_score, "\n")
    # elif user_input != "snake" or user_input != "water" or user_input != "gun":
    #     print("Invalid Input. Enter Again! \n")
    else:
        print("No one wins \n")

    i += 1
print("Computer scores ", computer_score, "points")
print("User scores ", user_score, "points")

if computer_score > user_score:
    print("Computer wins the game!")
elif user_score > computer_score:
    print("Congratulations User, You won the game!")
else:
    print("Game Tie. Play Again!")

