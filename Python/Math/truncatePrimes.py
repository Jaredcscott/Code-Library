'''
    @Author Jared Scott ☯
    Prob 37 of Project Euler 
'''
import math 
import time

def isPrime(numI):
    '''
        This function will return a true or false representing whether or not the given number ('num') is prime
    '''
    num = int(numI)
    if num < 0:
        num = -1 * num
    if all(num%i!=0 for i in range(2,int(math.sqrt(num)) + 1)) and num > 1:
        return True
    else:
        return False
    
def truncateLeft(num):
    #This function removes one character from the left of the given string 
    numStr = str(num) 
    num = numStr[1:]
    return num

def truncateRight(num):
    #this function removes one character from the right of the given string 
    numStr = str(num) 
    num = numStr[:-1]
    return num
    
def main():        
    primes = []
    for i in range(750000):
        if isPrime(i) and i > 10:
            primes.append(i)

    sumPrimes = []
    sumP = 0
    for prime in primes:
        addToSum = True 
        curNum = prime
        while len(str(curNum)) > 1:
            newNum = truncateLeft(curNum)
            if not isPrime(newNum):
               addToSum = False 
            curNum = newNum 
        curNum = prime
        while len(str(curNum)) > 1:
            newNum = truncateRight(curNum)
            if not isPrime(newNum):
               addToSum = False    
            curNum = newNum 

        if addToSum:
            sumPrimes.append(prime)
            sumP += prime

    print(sumP," : ",sumPrimes) 

if __name__ == '__main__':
    main()
