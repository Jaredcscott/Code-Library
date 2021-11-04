'''
    @Author Jared Scott ☯
    This file holds the needed definitions for an Item 
'''

class Item:
    def __init__(self,name,type,value):
        self.name = name 
        self.type = type
        self.value = value  
        
    def setValue(self,value):
        self.value = value 
        
    def getValue(self):
        return self.value
      
    def __str__(self):
        return "Item: " + str(self.name) + " of Type: " + str(self.type) + " Value: " + str(self.value)
