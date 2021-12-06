'''
    @Author Jared Scott ☯
    This script will solve the 46th problem for Project Euler 
    Finds Off composite numbers which cannot be written in the form num = prime + 2*(root^2)
'''
import math

def isPrime(num):
    # This function determines if the provided number is prime or not by doing a remainder calculation on all potential roots less than 1 + sqrt(val) 
    if all(num%i!=0 for i in range(2,int(math.sqrt(num)) + 1)):
        return True
    else:
        return False
        
def getLesserPrimes(num):
    # This function will generate a list of all prime numbers which are less than the given number 
    nums = []
    for val in range(num):
        if (isPrime(val)):
            nums.append(val)
    return nums 

def generateOddCompositeNums(limit):
    # This function will generate a list of all composite numbers from 1 until the limit provided 
    # Uses prime factor calculation 
    nums = []
    for val in range(limit+1):
        if (not isPrime(val)) and val % 2 != 0:
            nums.append(val)
    return nums
    
def testEquality(num,prime,root):
    # This function will test whether the given values cause the following equation to be true:
    # num = prime + (2*(root^2))
    if (num == (prime + (2 * (root * root)))):
        return True
    else:
        return False
    
def main():
    answer = []
    upperLimit = 7500
    limitRoot = int(math.sqrt(upperLimit))
    # Generating a list of odd composite numbers
    compNums = generateOddCompositeNums(upperLimit)
    count = 0
    for num in compNums:
        # Main problem solving loop,             
        # break statements inserted to save iterations as well as a status check every 150 values
        count += 1
        found = False # Equivalent equation found 
        # For each composite number, extract a list of lesser primes
        lesserPrimes = getLesserPrimes(num)
        for prime in lesserPrimes:
            # Loop trough lesser primes trying equality using roots less than the upper limit root
            for root in range(limitRoot):
                if testEquality(num,prime,root):
                    # Equality found
                    if (count % 150 == 0):
                        print(str(count) + " Status Check: " + str(num) + "=" + str(prime) + " + 2*" + str(root)+ "^2")
                    found = True 
                    break
                if found:
                    break
            if found:
                break
        if not found:
            # No equivalence found, adding value to final answer 
            answer.append(num)
            print("----------------------Equivalence not found: " + str(num))
    # All values processed printing first answer only.       
    print("Answer: " + str(answer[0])) 

if __name__ == '__main__':
    main()