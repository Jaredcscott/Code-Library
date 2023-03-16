file = open('input.dat','r')
lines = file.readlines()
outlines = []
count = 0
for line in lines:
    data = line.split(' ')
    if len(data) > 13:
        if (data[6] == 'Var') :
            col = data[13][:-2][0]
            row = data[13][:-2][1:]
            dVal = data[11].split(':')[:-1][0][1:-3]
            dQua = data[11].split(':')[-1][1:-2]
            outlines.append("Var:"+row+','+col+','+dVal+','+dQua+'\n') 
        elif (data[6] == 'DebugChannels') :
            dMes = ' '.join(data[8:-4])
            dLoc = data[-1][:-2]
            outlines.append("DEBUG:"+dLoc+','+dMes+'\n') 

file.close()        
file = open('outData.dat', "w")
for line in outlines:
    file.write(line) 
file.close()
