file = open('dataFile.dat','r')
lines = file.readlines()
output = open('processedData.dat','w')
col = 0
curRow = [None,None]
for line in lines:
    curVal = line.split(' ')[-3]
    num = str(curVal.split('(')[0])[1:-1]
    curRow[col] = num
    if col == 0:
        col = 1
    else:
        output.write(curRow[0] + "\t0\t" + curRow[1] + "\t0\t\n")
        for i in range(5):
            output.write('      \n')
        col = 0
    
    
    
