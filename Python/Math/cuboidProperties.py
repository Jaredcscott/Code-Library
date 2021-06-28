'''
    Jared Scott
    This script can be used to calculate the properties of a cuboid
'''

print("Welcome to the Cuboid Calculator!")
print("Please enter values in feet.")
length = eval(input("Enter the length: "))
width = eval(input("Enter the width: "))
height = eval(input("Enter the height: "))
volume = length * width * height
surfaceArea = 2 * ((length * width) + (length * height) + (height * width))
print("The entered cuboid has the properties of " + str(length) + " X " + str(width) + " X " + str(height) + "\nThe cuboid has a volume of: " + str(volume) + " cubic feet and a surface area of: " + str(surfaceArea) + " square feet" )