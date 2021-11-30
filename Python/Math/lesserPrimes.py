'''
  @Author Jared Scott ☯
'''

def getLesserPrimes(num):
    # This function will generate a list of all prime numbers which are less than the given number 
    nums = []
    for val in range(num):
        if (isPrime(val)):
            nums.append(val)
    return nums 

def isPrime(num):
    # This function determines if the provided number is prime or not by doing a remainder calculation on all potential roots less than 1 + sqrt(val) 
    if all(num%i!=0 for i in range(2,int(math.sqrt(num)) + 1)):
        return True
    else:
        return False
