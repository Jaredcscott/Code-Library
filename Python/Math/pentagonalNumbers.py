import math

pentagonalNums = [] 
masterNums = []

def generatePentagonalNumbers(limit):
    num = 1
    while num < limit:
        curNum = (num * ((3 * num) - 1)) / 2 
        pentagonalNums.append(int(curNum))
        num += 1
        
def compareNums(numA,numB):
    sum1 = numA + numB
    sub = abs(numA - numB) 
    return (sum1 in pentagonalNums and sub in pentagonalNums)
    
generatePentagonalNumbers(3000)
for numA in pentagonalNums:
    for numB in pentagonalNums:
        if compareNums(numA,numB):
            print(numA,numB,abs(numA-numB))
