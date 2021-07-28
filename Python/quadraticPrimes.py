'''
    @author Jared Scott 
    Not the most efficient algorithm. Takes a while to crunch through all combinations 
'''
import math 

def isPrime(num):
    '''
        This function will return a true or false representing whether or not the given number ('num') is prime
        
        Arguments: 
            (Integer) num: The number which you would like to test
            
        Output:
            True if the number is prime, or False if the number is not prime 
    '''
    if num < 0:
        num = -1 * num
    if all(num%i!=0 for i in range(2,int(math.sqrt(num)) + 1)):
        return True
    else:
        return False
        
        
def solve(limit,a,b):
    primes = []
    for n in range(limit+1):
        term1 = n * n 
        term2 = a * n 
        val = term1 + term2 + b
        if isPrime(val):
            primes.append(val)
        else:
            break 
    if len(primes) > 25:
        print("N: " + str(limit),"a: " + str(a),"b: " + str(b),len(primes),primes)
    return len(primes)
    
def find(limN):
    most = 0
    mostN = 0
    limA = 1000
    limB = 1602 
    for n in range(1,limN):
        for a in range(-1*(limA),limA):
            for b in range(-1*(limB),limB):
                len = solve(n,a,b)
                if len > most:
                    most = len
                    mostN = n
                    print("New Most Found!\nmost: " + str(most) + " n: " + str(n) + " a: " + str(a) + " b: " + str(b))
                #if n % 10 == 0:
                #    print("Finding. . .\nCurrent Value: " + str(n))
    print(mostN,most)
#solve(39,1,41) 
find(200)   
    
 