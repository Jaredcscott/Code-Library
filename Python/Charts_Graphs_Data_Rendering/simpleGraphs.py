import pylab
from numpy import polyfit, poly1d, linspace
import math

x = numpy.linspace(0, 15, 1000)
y = 12 * numpy.cos(4*x)
pylab.xlabel('x')
pylab.ylabel('12 * cos(4 * x)')
pylab.title('Graph of cosine as x varies')
pylab.plot(x,y)
pylab.show()

#Sin wave with a different color line 
x = numpy.linspace(0, 20, 1000) ## Gave some fun and mess around with these numbers
y = numpy.sin(x)

pylab.plot(x,y, '-r', label='redline')
pylab.legend()

#Graphing from data found in a data file 
#writing to a file
with open("Equations.txt", "w+") as f:#keep this line
    for i in range(21):
        y = (i - 4) ** 2 + 2
        f.write(str(i) + ',' + str(y) + "\n")
        
#Reading from a file
with open("Equations.txt", "r+") as file:
    lines = file.readlines()
    x = [float(line.split(',')[0]) for line in lines]
    y = [float((line.split(',')[1]).strip()) for line in lines]
    pylab.plot(x,y, "-b", label = 'f(x) = (x-4)^2 + 2')
    pylab.legend()
    pylab.show()
       
#Graph with a fit
#set points
x = [-2,-1,0,1,2]
y = [5,1,-1,0,4]

#find fit
fit = polyfit(x,y,2) # the 2 indicates "to the second degree", like a quadratic function
func = poly1d(fit)

#find new points from fit
x_fit = linspace(x[0], x[-1], 500)
y_fit = func(x_fit)

#plot
pylab.plot(x, y, 'o', x_fit, y_fit)
pylab.show()

#Graph with a fit from a data file
with open("Equations.txt", "r+") as file:
    #extracting data from "Equations.txt"
    lines = file.readlines()
    x = [float(line.split(',')[0]) for line in lines]
    y = [float((line.split(',')[1]).strip()) for line in lines]
    #Plotting data 
    pylab.plot(x,y, "-b", label = 'f(x) = (x-4)^2 + 2')
    
    #Identifying a linear fit
    fit = polyfit(x,y,1)
    func = poly1d(fit)
    x_fit = linspace(x[0], x[-1], 500)
    y_fit = func(x_fit)
    #Plotting linear fit
    pylab.plot(x_fit, y_fit, "-r", label=str(func))
    pylab.title('Plot of equation with linear fit')
    
    pylab.legend()
    pylab.show()