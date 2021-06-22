'''
Jared Scott
This program shows how a custom class can overload operators to achieve various programming goals. 
This allows an individual to create custom classes that can be operated on with traditional operators. 
This also shows how two objects can be compared to each other IE the __lt__ and __gt__ operators. 
'''

def main():
    obj1 = OperatorOverloading(10)
    obj2 = OperatorOverloading(4)
    obj3 = OperatorOverloading(1)
    print(obj1 - obj2) 
    print(obj2 + obj3) 
    print(obj3 * obj2)
    print(obj1)
    if (obj1 > obj2):
        print("Object 1 is larger than object 2") 
    else:
        print("Object 2 is larger than object 1")
    

class OperatorOverloading:
    def __init__(self,value):
        try:
            self.__value = int(value)
        except:
            print("Value must be an integer")
            
    def __add__(self,object2):
        return self.__value + object2.__value

    def __sub__(self,object2):
        return self.__value - object2.__value
        
    def __mul__(self,object2):
        return self.__value * object2.__value
        
    def __div__(self,object2):
        return self.__value / object2.__value

    def __lt__(self,object2):
        return self.__value < object2.__value

    def __gt__(self,object2):
        return self.__value > object2.__value

    def __eq__(self,object2):
        return self.__value == object2.__value

    def __len__(self):
        return len(str(self.__value))

    def __str__(self):
        return "The value of this object is: " + str(self.__value)
        
        
main()