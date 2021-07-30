'''
    @author Jared Scott
    Prob 50 of Project Euler Solved 7/28/21
    INCOMPLETE
'''
import math 
import time

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
        
primes = []
for i in range(1200):
    if isPrime(i):
        primes.append(i)

def findSum(num):
    index = primes.index(num)
    curPrimes = primes[:index]
    size = 1
    while size < index:
        curSum = 0 
        sumNums = []
        for i in range(size):
            curSum += curPrimes[i]
            sumNums.append(curPrimes[i])
            if curSum == num:
                print(sumNums)
                return
        print(curSum)
        size += 1
        

findSum(953)
    
start_time = time.time()


seconds = time.time() - start_time
minutes = 0 
while seconds > 60:
    minutes += 1
    seconds -= 60
print("Runtime: " + str(minutes) + ":" + (str(int(seconds)) if seconds>9 else "0"+ str(int(seconds))))   
    
 