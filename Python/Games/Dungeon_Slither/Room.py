class Room:
    def __init__(self,number,actors):
        self.number = number
        self.actors = actors
        self.is_start = False 
        self.is_end = False 
        
    def peek_in_room(self):
        for actor in self.actors:
            print(actor)   