'''
    RUN ME TO PLAY
    @Author Jared Scott
    This is the main file for Rat Slayer, adjust the parameters below to alter starting conditions.
'''
from rat_slayer_funcs_ver2 import *


play_game_again = "Y"


while play_game_again.upper() == "Y":
    exit = "N"
    print("\n\n\n")
    print("               ___         _____          ")
    print("              /   \    /\    |            ")
    print("              |___/   /__\   |            ")
    print("              | \    /    \  |            ")
    print("              |  \  /      \ |            ")
    print("       ____                    ___  ___   ")
    print("      |     |       /\  \   / |    /   \  ")
    print("      |___  |      /__\  \ /  |___ |___/  ")
    print("          | |     /    \  |   |    | \    ")
    print("      ____| |___ /      \ |   |___ |  \   ")
    print("                 -Jared Scott             ")
    print("\n\n          Make it to level 30 to win \nMaximize the python shell window for best results\n\n\n")

    #---------Adjust these values to alter starting conditions---------
    ratBodies = 0
    playerLife = 10
    experience = 0
    damage = 1
    level = 1
    gold = 10




    playerLife,ratBodies,level,experience,damage,gold,exit = rat_fight(playerLife,ratBodies,level,experience,damage,gold,exit)

    if level >= 5:
        (playerLife,ratBodies,level,experience,damage,gold,exit) = big_rat_fight(playerLife,ratBodies,level,experience,damage,gold,exit)

    if level >= 15:
        (playerLife,ratBodies,level,experience,damage,gold,exit) = dragon(playerLife,ratBodies,level,experience,damage,gold,exit)

    if level > 29:
        (playerLife,ratBodies,level,experience,damage,gold,exit) = boss_battle(playerLife,ratBodies,level,experience,damage,gold,exit)

    play_game_again = input("\n\nDo you want to play again?: Y or N ")

    if play_game_again.upper() == "N":
        play_game_again = "N"
        print("\n\nGAME EXITED\n\n")
    else:
        play_game_again = "Y"
