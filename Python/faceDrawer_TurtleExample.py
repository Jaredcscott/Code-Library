'''
Jared Scott
This program will draw a face then present the user with a menu to alter various
aspects of the face. The face will be redrawn after each selection with the desired
settings. The program will loop until the user decides to quit.
'''

import turtle


class Face:
    def __init__(self):
        self.__smile = True
        self.__happy = True
        self.__dark_eyes = True

    def draw_face(self):
        turtle.clear()
        self.__draw_head()
        self.__draw_eyes()
        self.__draw_mouth()

    def is_smile(self):
        return self.__smile

    def is_happy(self):
        return self.__happy

    def is_dark_eyes(self):
        return self.__dark_eyes

    def change_mouth(self):
        self.__smile = False if self.is_smile() else True
        self.draw_face()

    def change_emotion(self):
        self.__happy = False if self.is_happy() else True
        self.draw_face()

    def change_eyes(self):
        self.__dark_eyes = False if self.is_dark_eyes() else True
        self.draw_face()

    def __draw_head(self):
        color = "yellow" if self.is_happy() else "red"
        turtle.fillcolor(color)
        turtle.showturtle()
        turtle.speed(0)
        turtle.pensize(1)
        turtle.penup()
        turtle.goto(0,-100)
        turtle.pendown()
        turtle.seth(0)
        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()

    def __draw_eyes(self):
        color = "black" if self.is_dark_eyes() else "blue"
        turtle.fillcolor(color)
        turtle.penup()
        turtle.goto(-40,50)
        turtle.pendown()
        turtle.seth(180)
        turtle.begin_fill()
        turtle.circle(12.5)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(40,50)
        turtle.pendown()
        turtle.seth(180)
        turtle.begin_fill()
        turtle.circle(12.5)
        turtle.end_fill()

    def __draw_mouth(self):
        if self.is_smile():
            turtle.pensize(7)
            turtle.pencolor("black")
            turtle.penup()
            turtle.goto(-60,-30)
            turtle.pendown()
            turtle.seth(310)
            turtle.circle(80,100)
        else:
            turtle.pensize(7)
            turtle.pencolor("black")
            turtle.penup()
            turtle.goto(60,-50)
            turtle.pendown()
            turtle.seth(130)
            turtle.circle(80,100)


def main():
    face = Face()
    face.draw_face()

    done = False

    while not done:
        print("Change My Face")
        mouth = "frown" if face.is_smile() else "smile"
        emotion = "angry" if face.is_happy() else "happy"
        eyes = "blue" if face.is_dark_eyes() else "black"
        print("1) Make me", mouth)
        print("2) Make me", emotion)
        print("3) Make my eyes", eyes)
        print("0) Quit")

        menu = eval(input("Enter a selection: "))

        if menu == 1:
            face.change_mouth()
        elif menu == 2:
            face.change_emotion()
        elif menu == 3:
            face.change_eyes()
        else:
            break

    print("Thanks for Playing")

    turtle.hideturtle()
    turtle.done()


main()