import math 
import time

limit = 1000000

def shiftChar(num):
    numStr = str(num) 
    first = numStr[0]
    newStr = numStr[1:]+first
    return newStr

def isPrime(num):
    '''
        This function will return a true or false representing whether or not the given number ('num') is prime
    '''
    if num < 0:
        num = -1 * num
    if all(num%i!=0 for i in range(2,int(math.sqrt(num)) + 1)) and num > 1:
        return True
    else:
        return False
        
def isCircularPrime(num):
    if isPrime(num):
        numLen = len(str(num))
        for permutation in range(numLen+1):
            #print("Before: " ,num)
            num = shiftChar(num)
            #print("After: " ,num)
            if not isPrime(int(num)):
                return False           
        return True 
    return False 

start_time = time.time()    
circularPrimes = []
for num in range(limit):
    if isCircularPrime(num):
        circularPrimes.append(num)
seconds = time.time() - start_time
minutes = 0 
while seconds > 60:
    minutes += 1
    seconds -= 60
print("Runtime: " + str(minutes) + ":" + (str(int(seconds)) if seconds>9 else "0"+ str(int(seconds))))   
print("Solution Found! ",len(circularPrimes)," : ",circularPrimes) 