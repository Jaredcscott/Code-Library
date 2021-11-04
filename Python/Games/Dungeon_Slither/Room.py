'''
    @Author Jared Scott ☯
    This file stores the needed class defitions for a room in the dungeon
'''

class Room:
    def __init__(self,number,actors,width,height):
        self.number = number
        self.actors = actors
        self.is_start = False 
        self.is_end = False 
        self.grid = self.gen_grid(width,height)
        
        
    def peek_in_room(self):
        for actor in self.actors:
            print(actor)  
            
    def gen_grid(self, width, height):
        pass
            
class GridCell:
    def __init__(self,xpos,ypos,data):
        self.xpos = xpos
        self.ypos = ypos 
        self.data = data 
