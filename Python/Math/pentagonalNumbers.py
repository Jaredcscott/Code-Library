'''
    @Author Jared Scott 
    This script generates then compared pentagonal numbers 
'''

import math

def main():
    pentagonalNums = [] 
    masterNums = []
    limit = 3000
    
    generatePentagonalNumbers(limit,pentagonalNums)
    for numA in pentagonalNums:
        for numB in pentagonalNums:
            if compareNums(numA,numB):
                print(numA,numB,abs(numA-numB))

def generatePentagonalNumbers(limit,numList):
    #This function will fill the given numList with limit number of pentagonal numbers
    num = 1
    while num < limit:
        curNum = (num * ((3 * num) - 1)) / 2 
        numList.append(int(curNum))
        num += 1
        
def compareNums(numA,numB):
    sum1 = numA + numB
    sub = abs(numA - numB) 
    return ((sum1 in pentagonalNums) and (sub in pentagonalNums))
    
if __name__ == '__main__':
    main()
