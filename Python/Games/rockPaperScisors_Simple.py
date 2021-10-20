'''
    @Author Jared Scott
    This script plays a single instance of rock paper scissors
'''

import random
computersChoice = random.getrandbits(2)
playersChoice = int(input("Please enter the number corresponding with your\
 choice.\nscissor (0), rock (1), paper (2): "))

if computersChoice == 0:
    if playersChoice == 1:
        print("The computer is scissor. You are rock. You win!")
    elif playersChoice == 0:
        print("The computer is scissor. You are scissor. It is a draw")
    else:
        print("The computer is scissor. You are paper. You lose.")

if computersChoice == 1:
    if playersChoice == 2:
        print("The computer is rock. You are paper. You win!")
    elif playersChoice == 1:
        print("The computer is rock. You are rock. It is a draw")
    else:
        print("The computer is rock. You are scissor. You lose.")

if computersChoice == 2:
    if playersChoice == 0:
        print("The computer is paper. You are scissor. You win!")
    elif playersChoice == 2:
        print("The computer is paper. You are paper. It is a draw")
    else:
        print("The computer is paper. You are rock. You lose.")
        
if computersChoice == 3:
    print("LAME") 
