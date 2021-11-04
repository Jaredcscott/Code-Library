'''
    @Author Jared Scott ☯

    This program will play a door selection game, behind one door is a car and behind the other two are goats.
    The user will select a door, and then the "host" will reveal the location of one of the goats. The "host" will
    then ask the user if they would like to switch their door selection to the remaining door.
'''
import random

playAgain = "Y"

while playAgain.upper() == "Y":
    print("\n\nThere are three doors infront of you. Behind one of them is a new \
car.\nBehind the other two are goats.\nIf you can correctly guess the door \
that hides the car, the car is yours.")
    playersChoice = eval(input("\nWhich door do you choose? 1 2 or 3: "))
    car = random.randint(1,3)
    if car == 1:
        goat1 = 2
        goat2 = 3
    elif car == 2:
        goat1 = 1
        goat2 = 3
    elif car == 3:
        goat1 = 1
        goat2 = 2

    if playersChoice == 1 and (goat1 == 3 or goat2 == 3):
        print("\n\nYou have selected door #1, behind door #3 is a goat.")
        switchChoice = input("Do you want to switch your selection? Y or N: ").upper()
        if switchChoice == "Y":
            playersChoice = 2
    elif playersChoice == 1 and (goat1 == 2 or goat2 == 2):
        print("\n\nYou have selected door #1, behind door #2 is a goat.")
        switchChoice = input("Do you want to switch your selection? Y or N: ").upper()
        if switchChoice == "Y":
            playersChoice = 3
    elif playersChoice == 2 and (goat1 == 3 or goat2 == 3):
        print("\n\nYou have selected door #2, behind door #3 is a goat.")
        switchChoice = input("Do you want to switch your selection? Y or N: ").upper()
        if switchChoice == "Y":
            playersChoice = 1
    elif playersChoice == 2 and (goat1 == 1 or goat2 == 1):
        print("\n\nYou have selected door #2, behind door #1 is a goat.")
        switchChoice = input("Do you want to switch your selection? Y or N: ").upper()
        if switchChoice == "Y":
            playersChoice = 3
    elif playersChoice == 3 and (goat1 == 1 or goat2 == 1):
        print("\n\nYou have selected door #3, behind door #1 is a goat.")
        switchChoice = input("Do you want to switch your selection? Y or N: ").upper()
        if switchChoice == "Y":
            playersChoice = 2
    elif playersChoice == 3 and (goat1 == 2 or goat2 == 2):
        print("\n\nYou have selected door #3, behind door #2 is a goat.")
        switchChoice = input("Do you want to switch your selection? Y or N: ").upper()
        if switchChoice == "Y":
            playersChoice = 1

    if playersChoice == car:
        print("\n\nYou have chosen wisely! You have won a Tesla model X")
    else:
        print("\n\nYou have chosen unwisely.\nThe goat laughs at you.")

    playAgain = input("\n\nDo you want to play again? Y or N ").upper()
