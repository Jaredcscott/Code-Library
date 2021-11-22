'''
    Jared Scott ☯
    This program defines the main function for the shape drawing program.  
'''


import turtle
from Circle import *
from Rectangle import *

turtle.showturtle()
turtle.speed(0)
turtle.shape("turtle")

def main():
    drawShapes = True
    shapes = []
    colors = ["Red","Yellow","Blue","Green"]

    while drawShapes:
        selection = eval(input("\n1) Enter Circle\n2) Enter Rectangle\n3) Remove Shape\n4) Draw Shapes\n5) Exit\nPlease make a selection: "))
        infoList = []
        for i in shapes:
            infoList.append("(%i) "%(len(infoList)+1) + i.getInfo())

        if selection == 1:
            startX,startY = eval(input("\nPlease enter the center point for your circle: "))
            radius = input("Please enter a radius: ")
            colorValid = False
            while not colorValid:
                colorChoice = eval(input("1) Red\n2) Yellow\n3) Blue\n4) Green\nPlease select a color: "))
                if colorChoice == 1 or colorChoice == 2 or colorChoice == 3 or colorChoice == 4:
                    print("Valid color selection")
                    colorValid = True
                else:
                    print("Invalid color selection")
            circle = Circle(startX,startY,radius,colors[colorChoice-1])
            shapes.append(circle)
            infoList.append("(%i )"%(len(infoList)+1) + circle.getInfo())

        if selection == 2:
            startX,startY = eval(input("\nPlease enter the starting point for your rectangle: "))
            height = eval(input("Please enter a height: "))
            width = eval(input("Please enter a width: "))
            colorValid = False
            while not colorValid:
                colorChoice = eval(input("1) Red\n2) Yellow\n3) Blue\n4) Green\nPlease select a color: "))
                if colorChoice == 1 or colorChoice == 2 or colorChoice == 3 or colorChoice == 4:
                    print("Valid color selection")
                    colorValid = True
                else:
                    print("Invalid color selection")
            rectangle = Rectangle(startX,startY,height,width,colors[colorChoice-1])
            shapes.append(rectangle)


        if selection == 3:
            again = True
            while again:
                infoList = []
                for i in shapes:
                    infoList.append("(%i) "%(len(infoList)+1) + i.getInfo())
                if infoList == []:
                    print("No more shapes.")
                    again = False
                    break
                for i in infoList:
                    print(i)
                choice = eval(input("Please enter the number of the shape to be removed: "))
                shapes.pop(choice - 1)
                infoList.pop(choice - 1)
                inputValid = False
                while not inputValid:
                    choice1 = input("Remove another? Y or N: ")
                    if choice1.upper() == "N":
                        again = False
                        inputValid = True
                    elif choice1.upper() == "Y":
                        break
                    else:
                        print("")

        if selection == 4:
            turtle.clear()
            for i in shapes:
                i.draw()

        if selection == 5:
            drawShapes = False
            print("\nThank you!\nExiting system")
            turtle.hideturtle()
            turtle.done()

main()
