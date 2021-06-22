#@author Jared Scott

def isPrime(num):
    '''
        This function will return a true or false representing whether or not the given number ('num') is prime
        
        Arguments: 
            (Integer) num: The number which you would like to test
            
        Output:
            True if the number is prime, or False if the number is not prime 
    '''
    factors = []
    for i in range(int(num + 1/2)):
        for j in range(num + 1):
            if i * j == num:
                if i not in factors:
                    factors.append(i)
                if j not in factors:
                    factors.append(j)
            if len(factors) > 2:
                continue
    print(num," trying a factor")
    if len(factors) == 2:
        return True
    else:
        return False