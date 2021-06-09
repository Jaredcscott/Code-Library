from math import asin
import numpy as np
import matplotlib.pyplot as plt

def gen_spiral(points,xOffset=0, yOffset=0, incOffset=0, scale=.1):
    file = open("./coords.csv",'w')
    xs = []                          # Stores the x values for a graphic representation
    ys = []                          # Stores the y values for a graphic representation
    ox = xOffset
    oy = yOffset
    points = points
    offset= incOffset
    tau = (1+5**0.5)/2.0             # golden ratio approx = 1.618033989
    inc = (2-tau)*2*np.pi + offset
    theta = 0
    k = scale                        # scale factor
    for j in range(1,points+1):
        r = k*j**0.5
        theta += inc
        x = int(ox + r*np.cos(theta) * 450)
        y = int(oy + r*np.sin(theta) * 450)
        xs.append(x)
        ys.append(y)
        file.write(str(x)+','+str(y)+',0,3\n')
    file.close()

    plt.scatter(xs,ys)
    plt.title("Pattern Generated")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()