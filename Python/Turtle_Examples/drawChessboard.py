'''
    @Author Jared Scott ☯
    This program draws a chessboard using the turtle library
    The class Chessboard is defined, and all of its necessary methods.
'''

import turtle

def main():
    board = Chessboard(0,0)
    board.draw()
    
class Chessboard:
    def __init__(self,start_x,start_y,width = 250, height = 250):
        self.__startx = start_x
        self.__starty = start_y
        self.__width = width
        self.__height = height

    def draw(self):
        turtle.speed(0)
        self.__draw_chessboard()

    def __draw_chessboard(self):
        turtle.penup()
        turtle.goto(self.__startx,self.__starty)
        turtle.pendown()
        turtle.forward(self.__width)
        turtle.seth(90)
        turtle.forward(self.__height)
        turtle.seth(180)
        turtle.forward(self.__width)
        turtle.seth(270)
        turtle.forward(self.__height)
        turtle.seth(0)
        turtle.penup()
        self.__draw_all_rectangles()


    def __draw_all_rectangles(self):
        row = 0
        while row < 8 :
            rectangles = 0
            if row == 1 or row == 3 or row == 5 or row == 7:
                turtle.penup()
                turtle.goto(self.__startx,self.__starty)
                turtle.seth(90)
                turtle.forward(row * (self.__height/8))
                turtle.seth(0)
                turtle.forward(self.__width/8)
            if row == 2 or row == 4 or row == 6:
                turtle.penup()
                turtle.goto(self.__startx,self.__starty)
                turtle.seth(90)
                turtle.forward(row * (self.__height/8))
                turtle.seth(0)
            while rectangles < 4:
                self.__draw_rectangle()
                if rectangles == 3:
                    break
                turtle.forward(self.__width/8)
                rectangles += 1
            row += 1

    def __draw_rectangle(self):
        turtle.pendown()
        turtle.fillcolor("black")
        turtle.begin_fill()
        turtle.forward(self.__width/8)
        turtle.seth(90)
        turtle.forward(self.__height/8)
        turtle.seth(180)
        turtle.forward(self.__width/8)
        turtle.seth(270)
        turtle.forward(self.__height/8)
        turtle.end_fill()
        turtle.penup()
        turtle.seth(0)
        turtle.forward(self.__width/8)

if __name__ == '__main__':
    main()
