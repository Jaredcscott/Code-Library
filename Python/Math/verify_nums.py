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
    
def main():    
    inputFile = open("pandigital_nums.dat","r")
    outputFile = open("final_nums.dat","w")
    lines = inputFile.readlines()
    for line in lines:
        if (isPanDigital(int(line))):
            print(line, len(line))
            if len(line) == 10:
                line = "0" + line
                outputFile.write(str(line))
                continue
            outputFile.write(line)
        else:
            print("Not a pNum")
    print(isPanDigital(1122565))
    inputFile.close()
    outputFile.close()
    
if __name__ == '__main__':
    main()