'''
    @Author Jared Scott ☯
    This file holds the needed definitions for a Dungeon 
'''

from Actor import Actor, Player 
from Room import Room

class Dungeon:
    def __init__(self,difficulty):
        self.rooms = []
        self.actorCount = 0 
        self.roomNum = 0
        self.initialize_dungeon(difficulty)
        
    def initialize_dungeon(self,difficulty):
        if difficulty == 1:
            self.rooms = [Room(self.roomNum,self.gen_actors(3)) for I in range(3)]
        if difficulty == 2:
            self.rooms = [Room(self.roomNum,self.gen_actors(3)) for I in range(4)]
        if difficulty == 3:
            self.rooms = [Room(self.roomNum,self.gen_actors(3)) for I in range(5)]
        self.rooms[0].actors.append(Player(1))
    
    def gen_actors(self,count):
        actors = []
        for i in range(count):
            actors.append(Actor(self.actorCount))
            self.actorCount += 1
        return actors 
    
    def print_dungeon(self):
        for room in self.rooms:
            room.check_room()

     
        
dung = Dungeon(1) 
dung.print_dungeon()

