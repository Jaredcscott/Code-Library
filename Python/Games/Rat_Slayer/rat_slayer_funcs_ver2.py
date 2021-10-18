import random
import time


def rat_fight(playerLife,ratBodies,level,experience,damage,gold,exit):
    in_woods = 1
    in_town = 0
    print("                                           ")
    print("    /\                                     ")
    print("   /  \                   .---.            ")
    print("  /____\             (\./)      \........- ")
    print("  /    \            >'  '<   (__.'\"\"\"BP ")
    print(" /______\          _\"_'_\"_\"____________ ")
    print("   |  |   (\/)    /                        ")
    print("///|  |////||/////                         ")
    print("You are in the woods")
    print("A rat appears")
    whack = input("Do you want to attack? Y or N: \nEntering N will bring you to town ")
    if whack.upper() == "N":
        whack,playerLife,ratBodies,level,experience,damage,gold,in_town,exit = go_to_town(whack,playerLife,ratBodies,level,experience,damage,gold,in_town,exit)
    while in_woods == 1:
        while whack.upper() == "Y":
            ratsLife = 7
            hit = 3
            hit2 = 4
            hit3 = 5
            hit4 = 6
            while ratsLife > 0 and playerLife > 0 and whack.upper() == "Y":
                roll = random.randint(1,6)
                playerLife,level,experience,damage,gold = random_event(playerLife,level,experience,damage,gold,in_town)
                if roll == hit or roll == hit2 or roll == hit3 or roll == hit4:
                    ratsLife -= damage
                    print("You whacked the rat!! %s damage done!"%str(damage))
                    print("The rat's health is %s"%str(ratsLife))
                else:
                    playerLife -= 1
                    print("You missed. The rat hits you causing 1 damage!   :(")
                    print("Your health is %s"%str(playerLife))
                time.sleep(.25)
                if ratsLife <= 0:
                    print("You have defeated the rat!\n2 health gained\nOne experience gained!\nOne gold gained")
                    playerLife += 2
                    ratBodies += 1
                    experience += 1
                    gold += 1
                elif playerLife <= 0:
                    print("            ____           ")
                    print("          /     \          ")
                    print("      X  |  RIP  |         ")
                    print(" ,,,,,|,,|_______|,        ")
                    print("/                  \       \n\n")
                    print("The world goes black.......you have died")
                    print("the battle is finished.......\n\n")
                    print("You slayed %s rat(s)"%str(ratBodies))
                    exit = "Y"
                    results = (playerLife,ratBodies,level,experience,damage,gold,exit)
                    print("\nYou made it to level %s\n\n\n"%str(level))
                    return results
                    break
                if experience >= 5:
                    damage += 1
                    experience = 0
                    level += 1
                    playerLife += 4
                    print("     _        _            _   ")
                    print(" |  |_ \   / |_ |   |   | |_)  ")
                    print(" |_ |_  \_/  |_ |_   \_/  |    ")
                    print("\nYou have gained a level!!!\nYou are now level %s damage increased by 1\n\n"%str(level))
                if level >= 5:
                    print("The small rats are no match for you, they run off into the brush.....\nWithin the woods a deeper squeek approaches......\n\n")
                    results = (playerLife,ratBodies,level,experience,damage,gold,exit)
                    return results
                    break
            print("\n\nYour health is %s"%str(playerLife))
            print("You have %s gold"%str(gold))
            again = input("\n\nAnother rat appears, do you attack? N will bring you to town: Y or N ")
            if again.upper() == "N":
                in_town = 1
                whack,playerLife,ratBodies,level,experience,damage,gold,in_town,exit = go_to_town(whack,playerLife,ratBodies,level,experience,damage,gold,in_town,exit)
        if exit.upper() == "Y":
            results = (playerLife,ratBodies,level,experience,damage,gold,exit)
            return results
            break

def big_rat_fight(playerLife,ratBodies,level,experience,damage,gold,exit):
    in_woods = 1
    in_town = 0
    print("                (\,/)                      ")
    print("    /\          oo   ''//,         _       ")
    print("   /  \       ,/_;~,        \,    / '      ")
    print("  /____\      \"'  \    (    \    !        ")
    print("  /    \            ',|  \    |__.'        ")
    print(" /______\          _'~  '~----''___________")
    print("   |  |   (\/)    /                        ")
    print("///|  |////||/////                         ")
    print("You are in the woods")
    print("A massive rat appears")
    whack = input("Do you want to attack? Y or N: \nEntering N will bring you to town ")
    if whack.upper() == "N":
        whack,playerLife,ratBodies,level,experience,damage,gold,in_town,exit = go_to_town(whack,playerLife,ratBodies,level,experience,damage,gold,in_town,exit)
    while in_woods == 1:
        while whack.upper() == "Y":
            ratsLife = 30
            hit = 3
            hit2 = 4
            hit3 = 5
            hit4 = 6
            while ratsLife > 0 and playerLife > 0 and whack.upper() == "Y":
                playerLife,level,experience,damage,gold = random_event(playerLife,level,experience,damage,gold,in_town)
                roll = random.randint(1,7)
                if roll == hit or roll == hit2 or roll == hit3 or roll == hit4:
                    ratsLife -= damage
                    print("You whacked the rat!! %s damage done!"%str(damage))
                    print("The rat's health is %s"%str(ratsLife))
                else:
                    playerLife -= 3
                    print("You missed! the rat hits you causing 3 damage! :(")
                    print("Your health is %s"%str(playerLife))
                time.sleep(.25)
                if ratsLife <= 0:
                    print("You have defeated the rat!\n3 health gained\nTwo experience gained!\nTwo gold gained")
                    playerLife += 3
                    ratBodies += 1
                    experience += 2
                    gold += 2
                elif playerLife <= 0:
                    print("            ____      ")
                    print("          /     \     ")
                    print("      X  |  RIP  |    ")
                    print(" ,,,,,|,,|_______|,   ")
                    print("/                  \   ")
                    print("The world goes black.......you have died")
                    print("the battle is finished.......\n\n")
                    print("You slayed %s rat(s)"%str(ratBodies))
                    exit = "Y"
                    results = (playerLife,ratBodies,level,experience,damage,gold,exit)
                    print("\nYou made it to level %s\n\n\n"%str(level))
                    return results
                    break
                if exit.upper() == "Y":
                    break
                if experience >= 12:
                    damage += 1
                    experience = 0
                    level += 1
                    playerLife += 6
                    print("     _        _            _   ")
                    print(" |  |_ \   / |_ |   |   | |_)  ")
                    print(" |_ |_  \_/  |_ |_   \_/  |    ")
                    print("\nYou have gained a level!!!\nYou are now level %s damage increased by 1\n\n"%str(level))
                if level >= 15:
                    print("The rats have all been slain.....\nTime for a real challenge......\n\n")
                    results = (playerLife,ratBodies,level,experience,damage,gold,exit)
                    return results
                    break
            print("\n\nYour health is %s"%str(playerLife))
            print("You have %s gold"%str(gold))
            again = input("\n\nAnother rat appears, do you attack? N will bring you to town: Y or N ")
            if again.upper() == "N":
                in_town = 1
                whack,playerLife,ratBodies,level,experience,damage,gold,in_town,exit = go_to_town(whack,playerLife,ratBodies,level,experience,damage,gold,in_town,exit)
        if exit.upper() == "Y":
            results = (playerLife,ratBodies,level,experience,damage,gold,exit)
            return results
            break

def dragon(playerLife,ratBodies,level,experience,damage,gold,exit):
    in_woods = 1
    in_town = 0
    print("                                _/|__")
    print("            _,-------,         _/ -|  \_     /~>.")
    print("         _-~ __--~~/\  |      (  \   /  )   | / |")
    print("      _-~__--    //   \ \      \ *   * /   / | ||")
    print("   _-~_--       //     | |      \     /   | /  /|")
    print("  ~ ~~~~-_     //       \ \     |( \" )|  / | || /")
    print("          \   //         | |    | VWV | | /  ///")
    print("    |\     | //           \ \ _/      |/ | ./ |")
    print("    | |    |// __         _-~         \// |  /")
    print("   /  /   //_-~  ~~--_ _-~  /          |\// /")
    print("  |  |   /-~        _-~    (     /   |/ / /")
    print(" /   /           _-~  __    |   |____|/")
    print("|   |__         / _-~  ~-_  (_______  `\ ")
    print("|      ~~--__--~ /  _     \        __\)))")
    print(" \               _-~       |     ./  \ ")
    print("  ~~--__        /         /    _/     |")
    print("        ~~--___/       _-_____/      /")
    print("         _____/     _-_____/      _-~")
    print("      /^<  ___       -____         -____")
    print("         ~~   ~~--__      ``\--__       ``\ ")
    print("                    ~~--\)\)\)   ~~--\)\)\) ")
    print("You are in the woods")
    print("A DRAGON APPEARS!!!")
    whack = input("Do you want to attack? Y or N: \nEntering N will bring you to town ")
    if whack.upper() == "N":
        whack,playerLife,ratBodies,level,experience,damage,gold,in_town,exit = go_to_town(whack,playerLife,ratBodies,level,experience,damage,gold,in_town,exit)
    while in_woods == 1:
        while whack.upper() == "Y":
            ratsLife = 150
            hit = 3
            hit2 = 4
            hit3 = 5
            hit4 = 6
            while ratsLife > 0 and playerLife > 0 and whack.upper() == "Y":
                playerLife,level,experience,damage,gold = random_event(playerLife,level,experience,damage,gold,in_town)
                roll = random.randint(1,8)
                if roll == hit or roll == hit2 or roll == hit3 or roll == hit4:
                    ratsLife -= damage
                    print("You whacked the dragon!! %s damage done!"%str(damage))
                    print("The dragon's health is %s"%str(ratsLife))
                else:
                    playerLife -= 5
                    print("You missed the dragon, it hits you causing 5 damage! :(")
                    print("Your health is %s"%str(playerLife))
                time.sleep(.25)
                if ratsLife <= 0:
                    print("You have defeated the dragon!\n4 health gained\nFour experience gained!\nSeven gold gained")
                    playerLife += 4
                    ratBodies += 1
                    experience += 4
                    gold += 7
                elif playerLife <= 0:
                    print("            ____      ")
                    print("          /     \     ")
                    print("      X  |  RIP  |    ")
                    print(" ,,,,,|,,|_______|,   ")
                    print("/                  \   ")
                    print("The world goes black.......you have died")
                    print("the battle is finished.......\n\n")
                    print("You slayed %s creature(s)"%str(ratBodies))
                    exit = "Y"
                    results = (playerLife,ratBodies,level,experience,damage,gold,exit)
                    print("\nYou made it to level %s\n\n\n"%str(level))
                    return results
                    break
                if exit.upper() == "Y":
                    break
                if experience >= 15:
                    damage += 1
                    experience = 0
                    level += 1
                    playerLife += 10
                    print("     _        _            _   ")
                    print(" |  |_ \   / |_ |   |   | |_)  ")
                    print(" |_ |_  \_/  |_ |_   \_/  |    ")
                    print("\nYou have gained a level!!!\nYou are now level %s damage increased by 1\n\n"%str(level))
            print("\n\nYour health is %s"%str(playerLife))
            print("You have %s gold"%str(gold))
            if level >= 29:
                results = (playerLife,ratBodies,level,experience,damage,gold,exit)
                return results
                break
            again = input("\n\nAnother dragon appears, do you attack? N will bring you to town: Y or N ")
            if again.upper() == "N":
                in_town = 1
                whack,playerLife,ratBodies,level,experience,damage,gold,in_town,exit = go_to_town(whack,playerLife,ratBodies,level,experience,damage,gold,in_town,exit)
        if exit.upper() == "Y":
            results = (playerLife,ratBodies,level,experience,damage,gold,exit)
            return results
            break

def boss_battle(playerLife,ratBodies,level,experience,damage,gold,exit):
    in_woods = 1
    in_town = 0
    print("                                _/|__")
    print("            _,-------,         _/ -|  \_     /~>.                         ")
    print("         _-~ __--~~/\  |      (  \   /  )   | / |                         ")
    print("      _-~__--    //   \ \      \ *   * /   / | ||                         ")
    print("   _-~_--       //     | |      \     /   | /  /|                         ")
    print("  ~ ~~~~-_     //       \ \     |( \" )|  / | || /                        ")
    print("          \   //         | |    | VWV | | /  ///                          ")
    print("    |\     | //           \ \ _/      |/ | ./ |                           ")
    print("    | |    |// __         _-~         \// |  /  :                      :  ")
    print("   /  /   //_-~  ~~--_ _-~  /          |\// /   ::                    ::  ")
    print("  |  |   /-~        _-~    (     /   |/ / /     ::`.     .-""-.     .'::  ")
    print(" /   /           _-~  __    |   |____|/         : `.`-._ : '>': _.-'.' :  ")
    print("|   |__         / _-~  ~-_  (_______  `\        :`. `=._`'.  .''_.=' .':  ")
    print("|      ~~--__--~ /  _     \        __\)))        : `=._ `- '' -' _.-'.:   ")
    print(" \               _-~       |     ./  \            :`=._`=.    .='_.=':    ")
    print("  ~~--__        /         /    _/     |            `.._`.      .'_..'     ")
    print("        ~~--___/       _-_____/      /               `-.:      :.-'       ")
    print("         _____/     _-_____/      _-~                   :      :          ")
    print("      /^<  ___       -____         -____                `:.__.:'          ")
    print("         ~~   ~~--__      ``\--__       ``\              :    :           ")
    print("                    ~~--\)\)\)   ~~--\)\)\)             -'=  -'=          ")
    print("You are in the woods")
    print("A  large dragon appears and beside him is the Chicken king JERRY SPRINGER!!!!!")
    print("\n\n BEWARE, ONCE THIS BATTLE STARTS THERE WILL BE NO OPPORTUNITY TO GO TO TOWN\n\n")
    print("I SUGGEST YOU GO TO TOWN AND MAX OUT YOUR STATS IN THE SHOP")
    print("AT LEAST 45 DAMAGE and 850 HEALTH RECOMMENDED")
    whack = input("Do you want to attack? Y or N: \nEntering N will bring you to town ")
    if whack.upper() == "N":
        whack,playerLife,ratBodies,level,experience,damage,gold,in_town,exit = go_to_town(whack,playerLife,ratBodies,level,experience,damage,gold,in_town,exit)
    while in_woods == 1:
        while whack.upper() == "Y":
            dragondead = 0
            jerrydead = 0
            ratsLife = 600
            jerryLife = 1400
            hit = 3
            hit2 = 4
            hit3 = 5
            hit4 = 6
            while (ratsLife > 0 or jerryLife > 0) and playerLife > 0 and whack.upper() == "Y":
                playerLife,level,experience,damage,gold = random_event(playerLife,level,experience,damage,gold,in_town)
                roll = random.randint(1,8)
                roll2 = random.randint(1,9)
                if (roll == hit or roll == hit2 or roll == hit3 or roll == hit4) and ratsLife > 0:
                    ratsLife -= damage
                    print("You whacked the dragon!! %s damage done!"%str(damage))
                    print("The dragon's health is %s"%str(ratsLife))
                elif (roll == 1 or roll == 2 or roll == 7 or roll == 8) and ratsLife > 0:
                    playerLife -= 8
                    print("You missed the dragon, it hits you causing 8 damage! :(")
                    print("Your health is %s"%str(playerLife))

                if (roll2 == hit or roll2 == hit2 or roll2 == hit3 or roll2 == hit4) and jerryLife > 0:
                    jerryLife -= damage
                    print("You whacked Jerry!! %s damage done!"%str(damage))
                    print("The Jerry's health is %s"%str(jerryLife))
                elif (roll2 == 1 or roll2 == 2 or roll2 == 7 or roll2 == 8 or roll2 == 9) and jerryLife > 0:
                    playerLife -= 12
                    print("You missed Jerry, He hits you causing 12 damage! :(")
                    print("Your health is %s"%str(playerLife))
                time.sleep(.25)

                if ratsLife <= 0 and dragondead != 1:
                    print("\n\nYou have defeated the dragon!\n4 health gained\nFour experience gained!\nSeven gold gained")
                    playerLife += 4
                    ratBodies += 1
                    experience += 4
                    gold += 7
                    dragondead = 1
                if jerryLife <= 0 and jerrydead != 1:
                    print("\n\nYou have defeated Jerry!\n4 health gained\n\n")
                    playerLife +=4
                    ratBodies += 1
                    experience += 5
                    jerrydead = 1
                elif playerLife <= 0:
                    print("            ____      ")
                    print("          /     \     ")
                    print("      X  |  RIP  |    ")
                    print(" ,,,,,|,,|_______|,   ")
                    print("/                  \   ")
                    print("The world goes black.......you have died")
                    print("the battle is finished.......\n\n")
                    print("You slayed %s creature(s)"%str(ratBodies))
                    exit = "Y"
                    results = (playerLife,ratBodies,level,experience,damage,gold,exit)
                    print("\nYou made it to level %s\n\n\n"%str(level))
                    return results
                    break
                if exit.upper() == "Y":
                    break
                if experience >= 15:
                    damage += 1
                    experience = 0
                    level += 1
                    playerLife += 10
                    print("     _        _            _   ")
                    print(" |  |_ \   / |_ |   |   | |_)  ")
                    print(" |_ |_  \_/  |_ |_   \_/  |    ")
                    print("\nYou have gained a level!!!\nYou are now level %s damage increased by 1\n\n"%str(level))
            print("\n\nYour health is %s"%str(playerLife))
            print("You have %s gold"%str(gold))
            if dragondead == 1 and jerrydead == 1:
                print("\n\n\n\n\nThe great Jerry has been slain....\nThe dragons flee in terror at your awesome power\n\n")
                print("   ___________    ")
                print("  (\   YOU   /)   ")
                print("  (_\  WIN  /_)   ")
                print("     \_____/      ")
                print("      |   |       ")
                print("      /   \       ")
                print("     /_____\      ")
                print("\n\nYou have won the game!")
                print("Your level is %s"%str(level))
                print("Your health is %s"%str(playerLife))
                print("You slayed %s creature(s)"%str(ratBodies))
                print("\n\nThanks for playing! - Jared Scott")
                exit = "Y"
                whack = "N"
                break
        if exit.upper() == "Y":
            results = (playerLife,ratBodies,level,experience,damage,gold,exit)
            return results
            break

def store(playerLife,damage,gold):
    in_store = 1
    print("\n\n   Welcome to my humble store, please peruse my wares\n\n")
    print("    | P1 |       | P2 |       |  P3 |        |  P4 |     ")
    print("   / +15  \     /  +1  \     /  +35  \      /  + 3  \    ")
    print("  / health \   / damage \   /  health \    /  damage \   ")
    print("__\_5 gold_/___\_7_gold_/___\_10_gold_/____\_14_gold_/___")
    print(" ||                                                   || ")
    print(" ||                                                   || ")
    print(" ||                                                   || ")
    print("\n\n")
    print("Would you like to purchase any potions?\n\n")
    print("\nYou have %s gold"%str(gold))
    while in_store == 1:
        purchase = input("\nIf you do not want to purchase anything type 5\nEnter the number of the potion you would like to purchase (IE 1,2,3 or 4): ")
        if eval(purchase) == 1 and gold >= 5:
            playerLife += 15
            gold -= 5
            print("health increased by 10")
            print("Your health is %s"%str(playerLife))
            print("\nYou have %s gold"%str(gold))
        elif eval(purchase) == 1 and gold < 5:
            print("Not enough gold to purchase")

        if eval(purchase) == 2 and gold >= 7:
            if damage <= 45:
                damage += 1
                gold -= 7
                print("Damage increased by 1")
                print("Your damage is %s"%str(damage))
                print("\nYou have %s gold"%str(gold))
            else:
                print("You are at max damage")
        elif eval(purchase) == 2 and gold < 7:
            print("Not enough gold to purchase")


        if eval(purchase) == 3 and gold >= 10:
            playerLife += 35
            gold -= 10
            print("health increased by 25")
            print("Your health is %s"%str(playerLife))
            print("\nYou have %s gold"%str(gold))
        elif eval(purchase) == 3 and gold < 10:
            print("Not enough gold to purchase")


        if eval(purchase) == 4 and gold >= 14:
            if damage <= 45:
                damage += 3
                gold -= 14
                print("Damage increased by 3")
                print("Your damage is %s"%str(damage))
                print("\nYou have %s gold"%str(gold))
            else:
                print("You are at max damage")
        if eval(purchase) == 4 and gold < 14:
            print("Not enough gold to purchase")
        if eval(purchase) == 5:
            print("Thanks for stopping by my store! hope to see you again soon!")
            in_store = 0
            break
        stay = input("Do you want to stay in the store?: Y or N ")

        if stay.upper() == "N":
            print("Thanks for stopping by my store! hope to see you again soon!")
            in_store = 0
            break
    print("                                                                                             ")
    print("                                                                                             ")
    print("                                                                                             ")
    print("___________                                 ______________              _____ ___________    ")
    print(" /     /   \                               /    \ \     \ \            /  -  \   |   |   |   ")
    print("   /  /     \                             /  --- \    \    \          /   $   \        | |   ")
    print("_/__ /_______\                           /________\______\__\        /_________\__|______|   ")
    print("    |   INN  |                           | STORE   |   ___  |        |  ARENA  |        |    ")
    print("    |   __   |      ___            b_    |  _____  |  |_'_| |        |   ___   |        |    ")
    print("    |  |. |  |     |___|___/_ ('')-'     | | .|. | |        |        |  |.  |  |   _    |    ")
    print(" ___|__|__|__|,,,,,,( )  ( ) / \ \,,,,,,,| |  |  | |________|//\///\ |  |   |  |,,/ \,,,|,,,,")
    results = (playerLife,damage,gold)
    return results


def go_to_town(whack,playerLife,ratBodies,level,experience,damage,gold,in_town,exit):
    in_town = 1
    playerLife,level,experience,damage,gold = random_event(playerLife,level,experience,damage,gold,in_town)
    print("                                                                                             ")
    print("                                                                                             ")
    print("                                                                                             ")
    print("___________                                 ______________              _____ ___________    ")
    print(" /     /   \                               /    \ \     \ \            /  -  \   |   |   |   ")
    print("   /  /     \                             /  --- \    \    \          /   $   \        | |   ")
    print("_/__ /_______\                           /________\______\__\        /_________\__|______|   ")
    print("    |   INN  |                           | STORE   |   ___  |        |  ARENA  |        |      ")
    print("    |   __   |      ___            b_    |  _____  |  |_'_| |        |   ___   |        |      ")
    print("    |  |. |  |     |___|___/_ ('')-'     | | .|. | |        |        |  |.  |  |   _    |      ")
    print(" ___|__|__|__|,,,,,,( )  ( ) / \ \,,,,,,,| |  |  | |________|//\///\ |  |   |  |,,/ \,,,|,,,,\n")
    while in_town == 1:
        sleep = input("\nDo you want to sleep to recover health?: Y or N ")
        if sleep.upper() == "Y":
            print("      ()___                       _______  ")
            print("    ()//__/)_________________()  |_o_|_o_| ")
            print("    ||(___)//#/_/#/_/#/_/#()/||  |___o___| ")
            print("    ||----|#| |#|_|#|_|#|_|| ||  |___o___| ")
            print("    ||____|_|#|_|#|_|#|_|#||/||  |___o___| ")
            print("    ||    |#|_|#|_|#|_|#|_||      ||   ||  ")
        while sleep.upper() == "Y":
            if sleep.upper() == "Y" and playerLife <= level * 12 and level <= 20:
                print("\nSleeping...")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("You awaken from your slumber refreshed and ready to fight")
                print("15 health recovered")
                playerLife += 15
                print("Your health is %s"%str(playerLife))
            elif sleep.upper() == "Y" and playerLife <= level * 12 and level > 20:
                print("\nSleeping...")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("...")
                time.sleep(1)
                print("You awaken from your slumber refreshed and ready to fight")
                print("35 health recovered")
                playerLife += 35
                print("Your health is %s"%str(playerLife))
            elif sleep.upper() == "Y" and playerLife >= level * 12:
                print("You are not tired, You are ready to fight. \n        (You are at max health)")
            sleep = input("\nDo you want to sleep to recover health?: Y or N ")
            if sleep.upper() == "N":
                print("                                                                                             ")
                print("                                                                                             ")
                print("                                                                                             ")
                print("___________                                 ______________              _____ ___________    ")
                print(" /     /   \                               /    \ \     \ \            /  -  \   |   |   |   ")
                print("   /  /     \                             /  --- \    \    \          /   $   \        | |   ")
                print("_/__ /_______\                           /________\______\__\        /_________\__|______|   ")
                print("    |   INN  |                           | STORE   |   ___  |        |  ARENA  |        |    ")
                print("    |   __   |      ___            b_    |  _____  |  |_'_| |        |   ___   |        |    ")
                print("    |  |. |  |     |___|___/_ ('')-'     | | .|. | |        |        |  |.  |  |   _    |    ")
                print(" ___|__|__|__|,,,,,,( )  ( ) / \ \,,,,,,,| |  |  | |________|//\///\ |  |   |  |,,/ \,,,|,,,,")


        store_ques = input("\nDo you want to go to the store?: Y or N ")
        if store_ques.upper() == "Y":
            playerLife,damage,gold = store(playerLife,damage,gold)

        arena_ques = input("\nDo you want to enter the arena?: Y or N ")
        if arena_ques.upper() == "Y":
            playerLife,ratBodies,level,experience,damage,gold,exit = arena(playerLife,ratBodies,level,experience,damage,gold,exit)
            if playerLife <= 0:
                results = whack,playerLife,ratBodies,level,experience,damage,gold,in_town,exit
                return results
                break
        if exit.upper() == "Y":
            break

        to_woods = input("\nDo you want to go to the woods to fight?: Y or N ")
        if to_woods.upper() == "Y":
            if level < 5:
                print("                                           ")
                print("    /\                                     ")
                print("   /  \                   .---.            ")
                print("  /____\             (\./)      \........- ")
                print("  /    \            >'  '<   (__.'\"\"\"BP ")
                print(" /______\          _\"_'_\"_\"____________ ")
                print("   |  |   (\/)    /                        ")
                print("///|  |////||/////                         ")
                print("You are in the woods")
                print("A rat appears")
            if 5 <= level and level < 15:
                print("                (\,/)                      ")
                print("    /\          oo   ''//,         _       ")
                print("   /  \       ,/_;~,        \,    / '      ")
                print("  /____\      \"'  \    (    \    !        ")
                print("  /    \            ',|  \    |__.'        ")
                print(" /______\          _'~  '~----''___________")
                print("   |  |   (\/)    /                        ")
                print("///|  |////||/////                         ")
                print("You are in the woods")
                print("A massive rat appears")
            if 15 <= level and level < 29:
                print("                                _/|__")
                print("            _,-------,         _/ -|  \_     /~>.    ")
                print("         _-~ __--~~/\  |      (  \   /  )   | / |    ")
                print("      _-~__--    //   \ \      \ *   * /   / | ||    ")
                print("   _-~_--       //     | |      \     /   | /  /|    ")
                print("  ~ ~~~~-_     //       \ \     |( \" )|  / | || /   ")
                print("          \   //         | |    | VWV | | /  ///     ")
                print("    |\     | //           \ \ _/      |/ | ./ |      ")
                print("    | |    |// __         _-~         \// |  /       ")
                print("   /  /   //_-~  ~~--_ _-~  /          |\// /        ")
                print("  |  |   /-~        _-~    (     /   |/ / /          ")
                print(" /   /           _-~  __    |   |____|/              ")
                print("|   |__         / _-~  ~-_  (_______  `\             ")
                print("|      ~~--__--~ /  _     \        __\)))            ")
                print(" \               _-~       |     ./  \               ")
                print("  ~~--__        /         /    _/     |              ")
                print("        ~~--___/       _-_____/      /               ")
                print("         _____/     _-_____/      _-~                ")
                print("      /^<  ___       -____         -____             ")
                print("         ~~   ~~--__      ``\--__       ``\          ")
                print("                    ~~--\)\)\)   ~~--\)\)\)          ")
                print("You are in the woods")
                print("A DRAGON APPEARS!!!")
            if 29 <= level:
                print("                                _/|__")
                print("            _,-------,         _/ -|  \_     /~>.                         ")
                print("         _-~ __--~~/\  |      (  \   /  )   | / |                         ")
                print("      _-~__--    //   \ \      \ *   * /   / | ||                         ")
                print("   _-~_--       //     | |      \     /   | /  /|                         ")
                print("  ~ ~~~~-_     //       \ \     |( \" )|  / | || /                        ")
                print("          \   //         | |    | VWV | | /  ///                          ")
                print("    |\     | //           \ \ _/      |/ | ./ |                           ")
                print("    | |    |// __         _-~         \// |  /  :                      :  ")
                print("   /  /   //_-~  ~~--_ _-~  /          |\// /   ::                    ::  ")
                print("  |  |   /-~        _-~    (     /   |/ / /     ::`.     .-""-.     .'::  ")
                print(" /   /           _-~  __    |   |____|/         : `.`-._ : '>': _.-'.' :  ")
                print("|   |__         / _-~  ~-_  (_______  `\        :`. `=._`'.  .''_.=' .':  ")
                print("|      ~~--__--~ /  _     \        __\)))        : `=._ `- '' -' _.-'.:   ")
                print(" \               _-~       |     ./  \            :`=._`=.    .='_.=':    ")
                print("  ~~--__        /         /    _/     |            `.._`.      .'_..'     ")
                print("        ~~--___/       _-_____/      /               `-.:      :.-'       ")
                print("         _____/     _-_____/      _-~                   :      :          ")
                print("      /^<  ___       -____         -____                `:.__.:'          ")
                print("         ~~   ~~--__      ``\--__       ``\              :    :           ")
                print("                    ~~--\)\)\)   ~~--\)\)\)             -'=  -'=          ")
                print("You are in the woods")
                print("A dragon appears and beside him is the Chicken king JERRY SPRINGER!!!!!")

            whack = "Y"
            in_town = 0
            results = whack,playerLife,ratBodies,level,experience,damage,gold,in_town,exit
            return results
            break


def arena(playerLife,ratBodies,level,experience,damage,gold,exit):
    in_arena = 1
    print("Welcome to the arena!")
    print("                 /()                                            |`-.__/\__.-`| ")
    print("                / /                                             |    |  |    | ")
    print("               / /                                              |____o()o____| ")
    print(" /============| |------------------------------------------,    |___((<>))___| ")
    print("{=| / / / / / /|()}     }     }     }                        >  \    o\/o    / ")
    print(" \============| |------------------------------------------'     \   |  |   /  ")
    print("               \ \                                                \  |  |  /   ")
    print("                \ \                                                '.|  |.'    ")
    print("                 \()                                                 `__`      ")
    opponent = eval(input("\nLevel 5 Prize 2 gold (Enter 1)\nLevel 10 Prize 4 gold (Enter 2)\nLevel 15 prize 6 gold (Enter 3)\nLevel 20 prize 8 gold (Enter 4)\n\nEnter 5 to exit\nSelect an opponent (1,2,3 or 4): "))
    while in_arena == 1:
        if opponent == 5:
            print("                                                                                             ")
            print("                                                                                             ")
            print("                                                                                             ")
            print("___________                                 ______________              _____ ___________    ")
            print(" /     /   \                               /    \ \     \ \            /  -  \   |   |   |   ")
            print("   /  /     \                             /  --- \    \    \          /   $   \        | |   ")
            print("_/__ /_______\                           /________\______\__\        /_________\__|______|   ")
            print("    |   INN  |                           | STORE   |   ___  |        |  ARENA  |        |    ")
            print("    |   __   |      ___            b_    |  _____  |  |_'_| |        |   ___   |        |    ")
            print("    |  |. |  |     |___|___/_ ('')-'     | | .|. | |        |        |  |.  |  |   _    |    ")
            print(" ___|__|__|__|,,,,,,( )  ( ) / \ \,,,,,,,| |  |  | |________|//\///\ |  |   |  |,,/ \,,,|,,,,")
            results = playerLife,ratBodies,level,experience,damage,gold,exit
            return results
            break
        if opponent == 1:
            spiderLife = 10
            hit = 3
            hit2 = 4
            hit3 = 5
            hit4 = 6
            print("              (                  ")
            print("               )                 ")
            print("              (                  ")
            print("     / \    .-\"\"\"-.   / \     ")
            print("    / /\  \/  ,,,  \/  /\ \      ")
            print("    | /\  | ,;;;;;, |  /\ |      ")
            print("    / /\ \ \;-\"\"\"-;/ / /\ \   ")
            print("   / /   \ /   .   \ /   \ \     ")
            print("  ( | ,-__|  \ | /  |__-, | )    ")
            print("    / /`__\  .-.-.  /__`\ \      ")
            print("   / / /.-(_( ) ( )_)-.\ \ \     ")
            print("  ( \ |)   \ '---' /  (| / )     ")
            print("   `  (|              |) `       ")
            print("      \)              (/         ")
            print("A spider appears")
            while spiderLife > 0 and playerLife > 0:
                roll = random.randint(1,7)
                if roll == hit or roll == hit2 or roll == hit3 or roll == hit4:
                    spiderLife -= damage
                    print("You whacked the spider!! %s damage done!"%str(damage))
                    print("The spider's health is %s"%str(spiderLife))
                else:
                    playerLife -= 3
                    print("You missed! the spider hits you causing 3 damage! :(")
                    print("Your health is %s"%str(playerLife))
                time.sleep(.25)
                if spiderLife <= 0:
                    print("You have defeated the spider!\n2 health gained\nTwo gold gained\n")
                    playerLife += 2
                    ratBodies += 1
                    gold += 2
                if playerLife <= 0:
                    print("            ____      ")
                    print("          /     \     ")
                    print("      X  |  RIP  |    ")
                    print(" ,,,,,|,,|_______|,   ")
                    print("/                  \  ")
                    print("The world goes black.......you have died")
                    print("the battle is finished.......\n\n")
                    print("You slayed %s creature(s)"%str(ratBodies))
                    exit = "Y"
                    results = (playerLife,ratBodies,level,experience,damage,gold,exit)
                    print("\nYou made it to level %s\n\n\n"%str(level))
                    return results
                    break
                if exit.upper() == "Y":
                    break
            print("\n\nYour health is %s"%str(playerLife))
            print("You have %s gold\n\n"%str(gold))
            stay_Arena = input("Do you want to fight again?: Y or N ")
            if stay_Arena.upper() == "N":
                in_arena = 0

        if opponent == 2:
            life = 30
            hit = 3
            hit2 = 4
            hit3 = 5
            hit4 = 6
            print("    /|  |\            /|  |\       ")
            print("    /|  |\            /|  |\       ")
            print("   / |  | \          / |  | \      ")
            print("   | |  | |          | |  | |      ")
            print("   \  \/  /  __  __  \  \/  /      ")
            print("    \    /  / /  \ \  \    /       ")
            print("     \  /   \ \__/ /   \  /        ")
            print("     \  /   /      \   \  /        ")
            print("    _ \ \__/ O    O \__/ /  _       ")
            print("   \ \ \___          ___/ / /       ")
            print(" _  \ \___/  ______  \___/ /  _     ")
            print(" \ \  ----(          )----  / /     ")
            print("  \ \_____( ________ )_____/ /      ")
            print("    ~-----(          )-----~  __     ")
            print("     _____( ________ )_____   \ \    ")
            print("   / ,----(          )----, \_/ /    ")
            print("  / /     (  ______  )     \/   \    ")
            print("   ~       \        /       \   /    ")
            print("            \  __  /        / /     ")
            print("             \    /        / /      ")
            print("              \   \       / /       ")
            print("               \   ~----~  /        ")
            print("                \_________/         ")
            print("A scorpion appears")
            while life > 0 and playerLife > 0:
                roll = random.randint(1,7)
                if roll == hit or roll == hit2 or roll == hit3 or roll == hit4:
                    life -= damage
                    print("You whacked the scorpion!! %s damage done!"%str(damage))
                    print("The scorpion's health is %s"%str(life))
                else:
                    playerLife -= 3
                    print("You missed! the scorpion hits you causing 3 damage! :(")
                    print("Your health is %s"%str(playerLife))
                time.sleep(.25)
                if life <= 0:
                    print("You have defeated the scorpion!\n2 health gained\nFour gold gained\n")
                    playerLife += 2
                    ratBodies += 1
                    gold += 4
                if playerLife <= 0:
                    print("            ____      ")
                    print("          /     \     ")
                    print("      X  |  RIP  |    ")
                    print(" ,,,,,|,,|_______|,   ")
                    print("/                  \  ")
                    print("The world goes black.......you have died")
                    print("the battle is finished.......\n\n")
                    print("You slayed %s creature(s)"%str(ratBodies))
                    exit = "Y"
                    results = (playerLife,ratBodies,level,experience,damage,gold,exit)
                    print("\nYou made it to level %s\n\n\n"%str(level))
                    return results
                    break
            print("\n\nYour health is %s"%str(playerLife))
            print("You have %s gold\n\n"%str(gold))
            stay_Arena = input("Do you want to fight again?: Y or N ")
            if stay_Arena.upper() == "N":
                in_arena = 0

        if opponent == 3:
            lion = 50
            hit = 3
            hit2 = 4
            hit3 = 5
            hit4 = 6
            print("             .,  ,.                       ,.     ")
            print("           ,((')/))).                    (()     ")
            print("         '(.(()( )\")),                ((())     ")
            print("       \"___/,  \"/)))/).'               .))     ")
            print("      '.-.   \"(()(()()/^             ( (        ")
            print("       ' _)   /)()())(()'______.---._.' )        ")
            print("        '.   _  (()(()))..            ,'         ")
            print("          (() \  ()) ())(             )          ")
            print("              ((                .     /_         ")
            print("              /       \,     .-(     (_ )        ")
            print("            .'   \/    )___.'   \      )         ")
            print("           /    \-    /        _/'.-'  /         ")
            print("          (,(,.'     ))       (_ /    /          ")
            print("             (,(,(,_)         (,(,(,_)           ")
            while lion > 0 and playerLife > 0:
                roll = random.randint(1,7)
                if roll == hit or roll == hit2 or roll == hit3 or roll == hit4:
                    lion -= damage
                    print("You whacked the lion!! %s damage done!"%str(damage))
                    print("The lion's health is %s"%str(lion))
                else:
                    playerLife -= 3
                    print("You missed! the lion hits you causing 3 damage! :(")
                    print("Your health is %s"%str(playerLife))
                time.sleep(.25)
                if lion <= 0:
                    print("You have defeated the lion!\n4 health gained\nFour gold gained\n")
                    playerLife += 4
                    ratBodies += 1
                    gold += 6
                if playerLife <= 0:
                    print("            ____      ")
                    print("          /     \     ")
                    print("      X  |  RIP  |    ")
                    print(" ,,,,,|,,|_______|,   ")
                    print("/                  \  ")
                    print("The world goes black.......you have died")
                    print("the battle is finished.......\n\n")
                    print("You slayed %s creature(s)"%str(ratBodies))
                    exit = "Y"
                    results = (playerLife,ratBodies,level,experience,damage,gold,exit)
                    print("\nYou made it to level %s\n\n\n"%str(level))
                    return results
                    break
            print("\n\nYour health is %s"%str(playerLife))
            print("You have %s gold\n\n"%str(gold))
            stay_Arena = input("Do you want to fight again?: Y or N ")
            if stay_Arena.upper() == "N":
                in_arena = 0

        if opponent == 4:
            elephant = 100
            hit = 3
            hit2 = 4
            hit3 = 5
            hit4 = 6
            print("                            _                     ")
            print("                          .' `'.__                ")
            print("                         /      \ `'\"-,          ")
            print("        .-''''--...__..-/ .     |      \          ")
            print("      .'               ; :'     '.  a   |         ")
            print("     /                 | :.       \     =\        ")
            print("    ;                   \ :.      /  ,-.__;.-;`   ")
            print("   /|     .              '--._   /-.7`._..-;`     ")
            print("  ; |       '                |`-'      \  =|      ")
            print("  |/\        .   -' /     /  ;         |  =/      ")
            print("  (( ;.       ,_  .:|     | /     /\   | =|       ")
            print("   ) / `\     | `\"\"`;     / |    | /   / =/     ")
            print("     | ::|    |      \    \ \    \ `--' =/        ")
            print("    /  '/\    /       )    |/     `-...-`         ")
            print("   /    | |  `\    /-'    /;                      ")
            print("   \  ,,/ |    \   D    .'  \                     ")
            print("    `\"\"`   \  nnh  D_.-'L__nnh                  ")
            while elephant > 0 and playerLife > 0:
                roll = random.randint(1,7)
                if roll == hit or roll == hit2 or roll == hit3 or roll == hit4:
                    elephant -= damage
                    print("You whacked the elephant!! %s damage done!"%str(damage))
                    print("The elephant's health is %s"%str(elephant))
                else:
                    playerLife -= 7
                    print("You missed! the elephant hits you causing 7 damage! :(")
                    print("Your health is %s"%str(playerLife))
                time.sleep(.25)
                if elephant <= 0:
                    print("You have defeated the elephant!\n4 health gained\nEight gold gained\n")
                    playerLife += 4
                    ratBodies += 1
                    gold += 8
                if playerLife <= 0:
                    print("            ____      ")
                    print("          /     \     ")
                    print("      X  |  RIP  |    ")
                    print(" ,,,,,|,,|_______|,   ")
                    print("/                  \  ")
                    print("The world goes black.......you have died")
                    print("the battle is finished.......\n\n")
                    print("You slayed %s creature(s)"%str(ratBodies))
                    exit = "Y"
                    results = (playerLife,ratBodies,level,experience,damage,gold,exit)
                    print("\nYou made it to level %s\n\n\n"%str(level))
                    return results
                    break
            print("\n\nYour health is %s"%str(playerLife))
            print("You have %s gold\n\n"%str(gold))
            stay_Arena = input("Do you want to fight again?: Y or N ")
            if stay_Arena.upper() == "N":
                in_arena = 0
    print("                                                                                             ")
    print("                                                                                             ")
    print("                                                                                             ")
    print("___________                                 ______________              _____ ___________    ")
    print(" /     /   \                               /    \ \     \ \            /  -  \   |   |   |   ")
    print("   /  /     \                             /  --- \    \    \          /   $   \        | |   ")
    print("_/__ /_______\                           /________\______\__\        /_________\__|______|   ")
    print("    |   INN  |                           | STORE   |   ___  |        |  ARENA  |        |    ")
    print("    |   __   |      ___            b_    |  _____  |  |_'_| |        |   ___   |        |    ")
    print("    |  |. |  |     |___|___/_ ('')-'     | | .|. | |        |        |  |.  |  |   _    |    ")
    print(" ___|__|__|__|,,,,,,( )  ( ) / \ \,,,,,,,| |  |  | |________|//\///\ |  |   |  |,,/ \,,,|,,,,")
    results = playerLife,ratBodies,level,experience,damage,gold,exit
    return results


def random_event(playerLife,level,experience,damage,gold,in_town):
    random_num = random.randint(1,150)
    dragon_random = random.randint(1,75)

    if random_num == 4 or random_num == 122 or random_num == 72:
        print("\n\nRANDOM EVENT!!")
        print("  _______       ")
        print(" /_______\     ")
        print("    | |        ")
        print("    | |      \n")
        print("Mushrooms found")
        print("+5 Health\n\n")
        playerLife += 5

    if random_num == 6 or random_num == 21:
        print("\n\nRANDOM EVENT!!")
        print("   _ _ _ _   ")
        print("  | | |_| |  ")
        print("  \_|_|\ \/  ")
        print("   \    \/   ")
        print("    |   |    ")
        print("\nYou feel a burst of strength")
        print("Damage increased by 1\n\n")
        damage += 1

    if random_num == 110 or random_num == 28:
        print("\n\nRANDOM EVENT!!")
        print("   \   |   |   /   ")
        print(" \  \  _____  /  / ")
        print("  \  /       \  /  ")
        print(" __  \ \~~~/ / __  ")
        print("      \_|_|_/      ")
        print("    /  |   |  \    ")
        print("   /    \_/    \   ")
        print("                   ")
        print("Wisdom smiles upon you")
        print("2 experience gained\n\n")
        experience += 2

    if random_num == 115 or random_num == 77:
        print("\n\nRANDOM EVENT!!")
        print("  _____      ")
        print(" (     )___  ")
        print("(__________) ")
        print(" '  / /  '     ")
        print("    \ \ '  '   ")
        print("   ' \ \      ")
        print(" '   / /'  '    ")
        print("  ' / /  '     ")
        print("    \/        ")
        print("\nLightning strikes your helmet!")
        print("3 health lost  :( \n\n")
        playerLife -= 3

    if random_num == 30 or random_num == 85:
        print("\n\nRANDOM EVENT!!")
        print("     __________  _    ")
        print("   /__________ /___\  ")
        print("  |   |__|    |     | ")
        print("  |           | |_| | ")
        print("  |___________|_____| ")
        print("\nTreasure chest found!")
        print("5 gold found\n\n")
        gold += 5

    if random_num == 83 or random_num == 147:
        print("\n\nRANDOM EVENT!!")
        print("   |   |      ")
        print("     /  O     ")
        print("   ______     ")
        print("  /      \    ")
        print("\nYou are feeling weak")
        print("Damage reduced by 1\n\n")
        damage -= 1
        if damage <= 0:
            damage = 1


    if level >= 15 and (dragon_random == 16 or dragon_random == 24 or dragon_random == 30) and in_town != 1:
        print("\n\nRANDOM EVENT!!")
        print("     /    /    /  ")
        print("    /    /    /   ")
        print("   /    /    /    ")
        print("  /    /    /     ")
        print("\n The dragon slashes you causing devestating damage")
        print("Health reduced by 5\n\n")
        playerLife -= 5

    if level >= 15 and (dragon_random == 60 or dragon_random == 40) and in_town != 1:
        print("\n\nRANDOM EVENT!!")
        print("        __  __  ")
        print("       /  \/  \ ")
        print("       \______/ ")
        print("       /    /   ")
        print("      /\/\/     ")
        print("    /\/\/       ")
        print("   /___/_       ")
        print("  /      \      ")
        print("  \__/\__/      ")
        print("\n The dragon breaks one of your bones weakening you")
        print("damage reduced by 3\n\n")
        damage -= 3

    if level >= 29 and (dragon_random == 26 or dragon_random == 30 ) and in_town != 1:
        print("\n\nRANDOM EVENT!!")
        print("  __         __         ")
        print(" /  \ |   | /   |__|    ")
        print(" \__/  \_/  \__ |  |    ")
        print("\nJerry pecks you in the eye!!")
        print("Health reduced by 5\n\n")
        playerLife -= 5




    results = playerLife,level,experience,damage,gold
    return results