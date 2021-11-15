'''
    @Author Jared Scott ☯
This program defines the Circle class, and all of its needed methods. 
'''

import turtle

class Circle:
    def __init__(self,startX,startY,radius,color):
        self.__startx = startX
        self.__starty = startY
        self.__radius = int(radius)
        self.__color = str(color)
        self.__type = " Circle"

    def getInfo(self):
        info = str(self.__color + self.__type)
        return info

    def draw(self):
        turtle.penup()
        turtle.goto(self.__startx,self.__starty)
        turtle.seth(270)
        turtle.forward(self.__radius)
        turtle.seth(0)
        turtle.pendown()
        turtle.fillcolor(self.__color)
        turtle.begin_fill()
        turtle.circle(self.__radius)
        turtle.end_fill()
        turtle.penup()
