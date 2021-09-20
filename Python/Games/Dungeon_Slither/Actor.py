class Actor:
    def __init__(self,id,type=None):
        self.id = id
        self.type = type

    def __str__(self):
        return "Actor ID: " + str(self.id) + " " + str(self.type) 

class Player(Actor):
    def __init__(self, id):
        super().__init__(id,"Player")