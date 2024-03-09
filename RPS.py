import sys
import random
from enum import Enum


def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3
    player_choice = input(
        "Enter Your Play...\n1 for ROCK 🪨 \n2 for PAPER 📜\n3 for SCISSORS ✂️\n")

    if (player_choice not in ["1", "2", "3"]):
        print("You Must enter 1, 2 or 3.Try again!! ")
        return play_rps()
    else:
        player = int(player_choice)
    computer_choice = random.choice("123")
    computer = int(computer_choice)

    print("\nYou Chose " + str(RPS(player)).replace("RPS.", "")+".")
    print("\nPython Chose " + str(RPS(computer)).replace("RPS.", "")+".")

    if (player == 1 and computer == 3):
        print("You Win🥳🎉")
    elif (player == 2 and computer == 1):
        print("You Win🥳🎉")
    elif (player == 3 and computer == 2):
        print("You Win🥳🎉")
    elif (player == computer):
        print("Draw 🫨")
    else:
        print("Python Win 🐍")

    print("\nPlay Again?")
    while True:
        playagain = input("\n Enter Y for Yes \n Q for Quit\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break
    if playagain.lower() == "y":
        return play_rps()
    else:
        print("Thankyou for playing!!☆*: .｡. o(≧▽≦)o .｡.:*☆")
        sys.exit("Bye! 👋")


play_rps()
