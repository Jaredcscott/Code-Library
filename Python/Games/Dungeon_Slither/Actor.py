class Actor:
    def __init__(self,id,type=None):
        self.id = id
        self.type = type
        self.health = 10
        self.atk = 1 
        self.def = 1
    
    def setHealth(self,value):
        self.health = value
    
    def setAtk(self,value):
        self.atk = value
        
    def setDef(self,value):
        self.def = value
        
    def __str__(self):
        return "Actor ID: " + str(self.id) + " " + str(self.type) 

class Player(Actor):
    def __init__(self, id):
        super().__init__(id,"Player")
