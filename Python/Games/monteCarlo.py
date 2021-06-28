'''
Jared Scott
CS 1400
Assn 8
This program will play a door selection game, behind one door is a car and behind the other two are goats.
The user will select a door, and then the "host" will reveal the location of one of the goats. The "host" will
then ask the user if they would like to switch their door selection to the remaining door.
Once the user is done playing, the program will take their decision to stick with their original door choice,
or to change, and run a simulation with that decision 100000 times. During the simulation the users original door
selection will be random, as well as the door that hides the car. After 100000 iterations the program will display
the amount that the player would have won and lost, and a winning percentage.  
'''
import random

ITERATIONS = 100000
playAgain = "Y"
wins = 0
losses = 0
iteration = 0

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
print("\n\nRunning simulation 100,000 times with your selection to either stay\
\nwith your original door selection or to switch.\n\n")
while iteration < ITERATIONS:
    playersChoice = random.randint(1,3)
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
        if switchChoice == "Y":
            playersChoice = 2
    elif playersChoice == 1 and (goat1 == 2 or goat2 == 2):
        if switchChoice == "Y":
            playersChoice = 3
    elif playersChoice == 2 and (goat1 == 3 or goat2 == 3):
        if switchChoice == "Y":
            playersChoice = 1
    elif playersChoice == 2 and (goat1 == 1 or goat2 == 1):
        if switchChoice == "Y":
            playersChoice = 3
    elif playersChoice == 3 and (goat1 == 1 or goat2 == 1):
        if switchChoice == "Y":
            playersChoice = 2
    elif playersChoice == 3 and (goat1 == 2 or goat2 == 2):
        if switchChoice == "Y":
            playersChoice = 1
    if playersChoice == car:
        wins += 1
    else:
        losses += 1
    iteration +=1

winLossPer = round((wins/100000)*100,2)
print("Simulation finished.\n")
print("With your choice you would have won " + str(wins) + " times.")
print("With your choice you would have lost " + str(losses) + " times.")
print("Your winning percentage is " + str(winLossPer) + "%")