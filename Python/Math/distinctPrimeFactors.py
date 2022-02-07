from functools import reduce
import math 

def isPrime(num):
    '''
        This function will return a true or false representing whether or not the given number ('num') is prime
        
        Arguments: 
            (Integer) num: The number which you would like to test
            
        Output:
            True if the number is prime, or False if the number is not prime 
    '''
    if all(num%i!=0 for i in range(2,int(math.sqrt(num)) + 1)):
        return True
    else:
        return False

def factors(num, limit):  
    '''
    Found the reduce function here: https://stackoverflow.com/questions/6800193
    For all general purposes num and limit should be the same, adjusting the limit may reduce execution time (IE sqrt(num))
    Inner comprehension produces a tuple filled with the factor pairs found using the modulus operation
    Reduce function will apply the given function (in this case it is adding the factor lists) and discards duplicate entries
    '''
    return list(reduce(list.__add__,([i, num//i] for i in range(1,limit+ 1) if num % i == 0)))

def reduce_factors(factors):
    output = []
    for factor in factors:
        if factor not in output:
            output.append(factor) 
    return(output) 

check = []
for i in range(1,150000):
    all_factors = reduce_factors(factors(i,i))
    prime_factors = []
    for factor in all_factors:
        if (isPrime(factor) and factor != 1):
            prime_factors.append(factor)
    if(len(prime_factors) == 4): 
        check.append((i,prime_factors))
    if i % 2500 == 0:
        print("Finding Factors..." + str(i))

for index in range(len(check)-2):
    if check[index][0] == (check[index+1][0] - 1) and check[index][0] == (check[index+2][0] - 2) and check[index][0] == (check[index+3][0] - 3):
        print(check[index][0],check[index+1][0],check[index+2][0],check[index+3][0])
    if index % 2500 == 0:
        print("Working..." + str(index))
    

