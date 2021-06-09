'''
    This class can be used to navigate an undrawn 2d space with a turtle actor. 
    The turtle will record all points visited (accessible with the method <turtle>.getPoints())
'''

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