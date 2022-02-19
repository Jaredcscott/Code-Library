file = open('dataFile.dat','r')
lines = file.readlines()
output = open('processedData.dat','w')
for line in lines:
    output.write(line.strip() + "\t0\n")     
    #for i in range(5):
        #output.write(line.strip() + "\t0\n")   #Used to duplicate the current value 
    #    output.write("\n") #Used to add empty rows 
        
file.close()
output.close()
