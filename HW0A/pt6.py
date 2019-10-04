# Alexander Hay
# ME_469, HW0, Part A6
# Dataset 1, Particle Filter
# Measurement Model

import numpy as np
import pylab as p
import math

# robot
xytheta=np.array([
(2,3,0),
(0,3,0),
(1,-2,0)])

# landmark
xyland=np.array([
(1.88032539,-5.57229508,6),
(3.07964257,0.24942861,13),
(-1.04151642,2.80020985,17)])

smodel=np.zeros((3,2))
xy=np.zeros((3,2))

for i in range(len(xytheta)):
    smodel[i,0]=(pow(pow(xytheta[i,0]-xyland[i,0],2)+pow(xytheta[i,1]-xyland[i,1],2),0.5))
    smodel[i,1]=math.atan2((xyland[i,1]-xytheta[i,1]),(xyland[i,0]-xytheta[i,0]))-xytheta[i,2]

xy[0,0]=0+(smodel[0,0]*np.cos(smodel[0,1]))
xy[1,0]=xy[0,0]+(smodel[1,0]*np.cos(smodel[1,1]))
xy[2,0]=xy[1,0]+(smodel[2,0]*np.cos(smodel[2,1]))

xy[0,1]=0+(smodel[0,0]*np.sin(smodel[0,1]))
xy[1,1]=xy[0,1]+(smodel[1,0]*np.sin(smodel[1,1]))
xy[2,1]=xy[1,1]+(smodel[2,0]*np.sin(smodel[2,1]))

# A E S T H E T I C
p.title("Global x,y Position")
p.xlabel("x position (m)")
p.ylabel("y position (m)")

p.plot(xytheta[:,0],xytheta[:,1],'bo',label='robot position')
p.plot(xy[:,0],xy[:,1],'rx',label='calculated position')

for i in range(len(xy)):
    p.annotate(str(i),#[:-2], # coordinate label
    (xy[i,0],xy[i,1]), # coordinates for label
    textcoords="offset points", # how to position text
    xytext=(-4,-10), # distance from text to points (x,y)
    ha='center') # horizontal adjustment; left, right, or center

    p.annotate(str(i),#[:-2], # coordinate label
    (xytheta[i,0],xytheta[i,1]), # coordinates for label
    textcoords="offset points", # how to position text
    xytext=(-4,-10), # distance from text to points (x,y)
    ha='center') # horizontal adjustment; left, right, or center

p.legend(loc='best')

for i in range(len(xy)):
    print 'point '+str(i)
    print 'x difference: '+str(abs(xytheta[i,0]-xy[i,0]))
    print 'y difference: '+str(abs(xytheta[i,1]-xy[i,1]))
    print

p.show()
