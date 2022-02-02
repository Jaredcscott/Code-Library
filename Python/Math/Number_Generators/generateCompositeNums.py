'''
    @Author Jared Scott ☯
    These functions can be used to generate a list of all composite numbers 
'''
import math

def isPrime(num):
    # This function determines if the provided number is prime or not by doing a remainder calculation on all potential roots less than 1 + sqrt(val) 
    if all(num%i!=0 for i in range(2,int(math.sqrt(num)) + 1)):
        return True
    else:
        return False

def generateCompositeNums(limit):
    # This function will generate a list of all composite numbers from 1 until the limit provided 
    # Uses prime factor calculation 
    nums = []
    for val in range(limit+1):
        if (not isPrime(val)):
            nums.append(val)
    return nums
