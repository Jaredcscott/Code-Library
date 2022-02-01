def isPanDigital(num):
    nums = []
    duplicateNums = False
    numStr = str(num)
    numLen = len(numStr)
    for char in numStr:
        if char in nums:
            return(False)
        else:
            nums.append(char) 
          
    nums.sort()
    if nums == ['0','1','2','3','4','5','6','7','8','9'] or nums == ['1','2','3','4','5','6','7','8','9']:
        return(True)
    return(False)      
        
def check_divisibility(num,primes):
    numStr = str(num) 
    check = []
    for digit in range(1,len(str(num))-2):
        check.append(int(numStr[digit] + numStr[digit+1] + numStr[digit+2]))
    allTrue = False 
    index = 0
    for substring in check:
        if (substring % primes[index] == 0):
            print(str(substring) + " % " + str(primes[index]) + " = 0")
            allTrue = True 
        else:
            allTrue = False
        index += 1
    return(allTrue)
    
def generate_pandigital_nums(limit):
    val = 1239999998
    count = 0
    pandigital_nums = []
    while val < limit:
        if isPanDigital(val):
            pandigital_nums.append(val)
        val += 1
        count += 1
        if count % 250000 == 0:
            print("Working...Last value tried: " + str(val))
    return(pandigital_nums)
    
def main():
    pandigital_nums = generate_pandigital_nums(9999999999)
    print(pandigital_nums[0:10])
    divisors = [2,3,5,7,11,13,17]
    outputFile = open("pandigital_nums.dat","w")
    for num in pandigital_nums:
        outputFile.write(str(num) + "\n")
    outputFile.close()
    
if __name__ == '__main__':
    main()
