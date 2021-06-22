'''
Jared Scott
This program defines the rectangle class, and all of its needed methods.
'''

import turtle

class Rectangle:
    def __init__(self,startX,startY,height,width,color):
        self.__startx = startX
        self.__starty = startY
        self.__height = height
        self.__width = width
        self.__color = str(color)
        self.__type = " Rectangle"

    def getInfo(self):
        info = str(self.__color + self.__type)
        return info

    def draw(self):
        turtle.penup()
        turtle.goto(self.__startx,self.__starty)
        turtle.seth(0)
        turtle.pendown()
        turtle.fillcolor(self.__color)
        turtle.begin_fill()
        turtle.forward(self.__width)
        turtle.left(90)
        turtle.forward(self.__height)
        turtle.left(90)
        turtle.forward(self.__width)
        turtle.left(90)
        turtle.forward(self.__height)
        turtle.end_fill()
        turtle.penup()