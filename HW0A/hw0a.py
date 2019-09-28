# Alexander Hay
# ME_469, HW0, Part A
# Filtering Algorithms
# Dataset 1, Particle Filter

import numpy as np
import matplotlib.pyplot as plt
import pylab as p
import math

barcodes=np.loadtxt('ds1_Barcodes.dat') #
groundtruth=np.loadtxt('ds1_Groundtruth.dat') # position data from motion capture (may be taken as known information for filtering)
landmark=np.loadtxt('ds1_Landmark_Groundtruth.dat') # landmark data
measurement=np.loadtxt('ds1_Measurement.dat') # position data measureed from robot
odometry=np.loadtxt('ds1_Odometry.dat') # time, forward v, angular v, measured from robot

initialx=0.98038490
initialy=-4.99232180
initialrad=1.44849633
initialt=1288971842.041

def odo():

    displacement =np.zeros((len(odometry),1)) # 1D array to hold calculated displacement values

    for i in range(len(odometry)):
        if i==0:
            displacement[i]=odometry[i,1]*(odometry[i,0]-initialt)
        else:
            displacement[i]=odometry[i,1]*(odometry[i,0]-odometry[i-1,0])

def main():

    # plots position data from motion capture
    p.plot(groundtruth[:,1],groundtruth[:,2])

    # plots landmark positions
    p.plot(landmark[:,1],landmark[:,2],'rx')

    # plots position data measured from robot
    x=np.cos(measurement[:,3])*measurement[:,2]
    y=np.sin(measurement[:,3])*measurement[:,2]

    odo()
    #p.plot(x,y)

    p.show()

main()
