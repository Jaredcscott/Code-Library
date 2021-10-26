'''
    @Author Jared Scott
    This program will take inputs from the user, namely the sides and length of a given
    polygon. the program will perform some calculations and output the area of the polygon
    to the user.
'''
import math

def main():
    numOfSides = eval(input("Enter the number of sides: "))
    sideLength = eval(input("Enter the side length: "))

    area = (numOfSides * math.pow(sideLength,2))/(4 * math.tan(math.pi/numOfSides))

    print("The area of the polygon is: {0}".format(str(area)))

if __name__ == '__main__':
        main()
