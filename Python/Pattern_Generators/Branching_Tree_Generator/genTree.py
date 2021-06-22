import matplotlib.pyplot as plt
import math
'''
    This generator will generate tree like fractal structures. 
    The coordinates will be displayed after generation on a scatter plot, but the actual coordinates will be stored in a file called coords.csv
    
    To use:
        Adjust the values below (MINIMUM_BRANCH_LENGTH, branchLen, armLen, angle) then run the script within any python terminal 
'''

xs = []                          # Stores the x values for a graphic representation
ys = []                          # Stores the y values for a graphic representation
exampleArgs = {'sixToOne':[60,10,60],'phiAndPi':[16,3.14,60]}

MINIMUM_BRANCH_LENGTH = 5
branchLen = 60      #Set These Values 
armLen = 10         #Set These Values 
angle = 60          #Set These Values 

def build_tree(file, turtle, branch_length, shorten_by, angle):
  global xs 
  global ys
  if branch_length > MINIMUM_BRANCH_LENGTH:
    turtle.forward(branch_length/4)
    file.write(str(int(turtle.xcor())*1.5)+','+str(int(turtle.ycor())* 1.5) +'\n')
    turtle.forward(branch_length/2)
    file.write(str(int(turtle.xcor())*1.5)+','+str(int(turtle.ycor())* 1.5) + '\n')
    turtle.forward(branch_length/4)
    new_length = branch_length - shorten_by    
    turtle.left(angle)
    build_tree(file, turtle, new_length, shorten_by, angle)  
    turtle.right(angle * 2)
    build_tree(file, turtle, new_length, shorten_by, angle)    
    turtle.left(angle)
    x = int(turtle.xcor()*1.5)
    y = int(turtle.ycor()* 1.5)
    xs.append(x)
    ys.append(y)
    file.write(str(x)+','+str(y)+'\n')
    turtle.backward(branch_length)

def gen_tree(branchLen,armLen,angle):
    file = open("./coords.csv",'w')
    file.truncate(0)
    tree = UndrawnTurtle()
    tree.setheading(90)
    build_tree(file, tree, branchLen,armLen,angle)
    tree.goto(0,0)
    tree.setheading(180)
    build_tree(file, tree, branchLen,armLen,angle)
    tree.goto(0,0)
    tree.setheading(270)
    build_tree(file, tree, branchLen,armLen,angle)
    tree.goto(0,0)
    tree.setheading(0)
    build_tree(file, tree, branchLen,armLen,angle)
    file.close()
    plt.scatter(xs,ys)
    plt.title("Pattern Generated")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

class UndrawnTurtle():
    def __init__(self):
        #Turtle starts at the origin facing right
        self.x, self.y, self.angle = 0.0, 0.0, 0.0
        self.pointsVisited = [] #stores a list of visited points  
        self._visit()

    def position(self):
        #Returns a list of the form [x,y]
        return [self.x, self.y]

    def goto(self, x, y = None):
        '''
            Used to instantaneously set the position of the turtle
            Can accept individual coordinates, a list of the form [x,y], or a tuple of the form (x,y)
        '''
        if y == None:
            self.x = x[0]
            self.y = x[1]
        else:
            self.x = x
            self.y = y
        self._visit()

    def xcor(self):
        #Returns the x coordinate 
        return self.x

    def ycor(self):
        #Returns the y coordinate 
        return self.y

    def forward(self, distance):
        #Moves the turtle forward in the heading direction (angle) 
        angle_radians = math.radians(self.angle)     #Conversion to radians 
        self.x += math.cos(angle_radians) * distance #Calculating the x portion of the move
        self.y += math.sin(angle_radians) * distance #Calculating the y portion of the move 
        self._visit()

    def backward(self, distance):
        #Moves the turtle backward
        self.forward(-distance)

    def right(self, angle):
        '''
            DOES NOT TRAVERSE RIGHT!!! 
            Adjusts the heading angle of the turtle, turning clockwise 
        '''
        self.angle -= angle

    def left(self, angle):
        '''
            DOES NOT TRAVERSE LEFT!!!
            Adjusts the heading angle of the turtle, turning counter-clockwise
        '''
        self.angle += angle

    def _visit(self):
        #Records the location within the pointsVisited array
        self.pointsVisited.append(self.position())
        
    def setheading(self,angle):
        '''
            Sets the heading angle of the turtle using a polar coordinate system.
            90  : UP
            180 : Left 
            270 : Down
            0   : Right
        '''
        self.angle = angle
      
    def getPoints(self):
        #Used to retrieve the visited points 
        return self.pointsVisited
      
gen_tree(branchLen,armLen,angle)