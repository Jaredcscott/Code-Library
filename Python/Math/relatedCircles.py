'''
    @Author Jared Scott ☯
    This script will determine the relationship between two circles. 
'''

import math
import turtle

def main():
    turtle.shape("turtle")
    turtle.speed(20)
    x1,y1,radius1 = eval(input("Please enter the coordinates of the first circle and its radius seperated by commas (eg 5,10,30): "))
    x2,y2,radius2 = eval(input("Please enter the coordinates of the second circle and its radius seperated by commas (eg 4,7,15): "))
    distance = float(((x2-x1)**2 + (y2 - y1)**2)**(1/2))
    if distance < radius1 and distance + radius2 < radius1:
        print("Circle 2 is fully inside of circle 1.")
    elif distance < radius2 and distance + radius1 < radius2:
        print("Circle 1 is fully inside of circle 2.")
    elif distance > radius1 + radius2 or distance == radius1 + radius2:
        print("The circles do not overlap.")
    elif radius1 > distance or radius2 > distance:
        print("The circles overlap.")
    '''
    For fun and for testing.
    '''
    if radius1 >= radius2:
        turtle.showturtle()
        turtle.penup()
        turtle.goto(x1,y1)
        turtle.fillcolor("green")
        turtle.seth(-90)
        turtle.forward(radius1)
        turtle.seth(0)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(radius1)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(x2,y2)
        turtle.fillcolor("blue")
        turtle.seth(-90)
        turtle.forward(radius2)
        turtle.seth(0)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(radius2)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(x2,y2)
        turtle.write("(" + str(x2) + "," + str(y2) + ")")
        turtle.goto(x1,y1)
        turtle.write("(" + str(x1) + "," + str(y1) + ")")
        turtle.hideturtle()
    elif radius2 > radius1:
        turtle.showturtle()
        turtle.penup()
        turtle.goto(x2,y2)
        turtle.fillcolor("blue")
        turtle.seth(-90)
        turtle.forward(radius2)
        turtle.seth(0)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(radius2)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(x1,y1)
        turtle.fillcolor("green")
        turtle.seth(-90)
        turtle.forward(radius1)
        turtle.seth(0)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(radius1)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(x1,y1)
        turtle.write("(" + str(x1) + "," + str(y1) + ")")
        turtle.hideturtle()
        turtle.goto(x2,y2)
        turtle.write("(" + str(x2) + "," + str(y2) + ")")
if __name__ == '__main__':
    main()
