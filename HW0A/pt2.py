# Alexander Hay
# ME_469, HW0, Part A
# Filtering Algorithms
# Dataset 1, Particle Filter

import numpy as np
import pylab as p
import math

# timestamp, velocity, angular velocity
odo=[(0,0.5,0),
(1,0,(-1/(2*math.pi))),
(2,0.5,0),
(3,0,(1/(2*math.pi))),
(4,0.5,0)]

odo=np.array(odo)

# array of x, y, theta values
xytheta=np.zeros((len(odo),3))

xytheta[0,0]=0
xytheta[0,1]=0
xytheta[0,2]=0

for i in range(len(odo)):
    time=1 # delta t is always 1 second
    vel=odo[i,1] # velocity data

    xytheta[i,2]=(odo[i,2]*time)+xytheta[i-1,2] # calculates theta value and adds to previous value
    xytheta[i,0]=xytheta[i-1,0]+(vel*np.cos(xytheta[i,2])*time) # calculates x and adds to previous value
    xytheta[i,1]=xytheta[i-1,1]+(vel*np.sin(xytheta[i,2])*time) # calculates y and adds to previous value

# reset origin values since they were overwritten
# This is not the ideal solution, but it works and displays the data correctly
# known bug where the second x position annotates as being 0, but graphically shows 0.5
# graph is correct. I don't know how to fix this
xytheta[0,0]=0
xytheta[0,1]=0

p.title("Position over Time")
p.xlabel("x position (m)")
p.ylabel("y position (m)")
p.xlim(-0.25,1.75)

for i in range(len(xytheta)):
    p.annotate(str(xytheta[i,0])[:-2], # coordinate label
    (xytheta[i,0],xytheta[i,1]), # coordinates for label
    textcoords="offset points", # how to position text
    xytext=(-4,-10), # distance from text to points (x,y)
    ha='center') # horizontal adjustment; left, right, or center

p.plot(xytheta[:,0],xytheta[:,1])

p.show()
