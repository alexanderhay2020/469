# Alexander Hay
# ME_469, HW0, Part A2
# Dataset 1, Particle Filter
# Motion Model

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

for i in range(len(odo)):
    time=1 # delta t is always 1 second
    vel=odo[i,1] # velocity data

    xytheta[i,2]=(odo[i,2]*time)+xytheta[i-1,2] # calculates theta value and adds to previous value
    xytheta[i,0]=xytheta[i-1,0]+(vel*np.cos(xytheta[i,2])*time) # calculates x and adds to previous value
    xytheta[i,1]=xytheta[i-1,1]+(vel*np.sin(xytheta[i,2])*time) # calculates y and adds to previous value

xytheta[0,0]=0
xytheta[0,1]=0
# this reset origin values since they were overwritten
# This is not the ideal solution, but it works and displays the line correctly

# A E S T H E T I C
p.title("Position over Time")
p.xlabel("x position (m)")
p.ylabel("y position (m)")
p.xlim(-0.25,1.75)

p.plot(xytheta[:,0],xytheta[:,1])

p.show()
