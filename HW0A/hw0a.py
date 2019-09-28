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

    # 2D array to hold calculated displacement and theta values, another for x&Y values
    displacement=np.zeros((len(odometry),2))
    delta=np.zeros((len(odometry),2))

    # calulates mometary displacement and theta
    for i in range(len(odometry)):
        if i==0:
            displacement[i,0]=odometry[i,1]*(odometry[i,0]-initialt) # finds displacement
            displacement[i,1]=odometry[i,2]*(odometry[i,0]-initialt) # finds delta theta
        else:
            displacement[i,0]=odometry[i,1]*(odometry[i,0]-odometry[i-1,0]) # finds displacement
            displacement[i,1]=odometry[i,2]*(odometry[i,0]-odometry[i-1,0]) # findsa delta theta

    # translates displacement and theta into x & y coordinates
    deltax=np.cos(displacement[:,1])*displacement[:,0]
    deltay=np.sin(displacement[:,1])*displacement[:,0]

    #delta[:,0]=np.cos(displacement[:,1])*displacement[:,0]
    #delta[:,1]=np.sin(displacement[:,1])*displacement[:,0]

    delta[0,0]=initialx
    delta[0,1]=initialy

    for i in range(1,len(delta)):
        delta[i,0]=delta[i-1,0]+deltax[i]
        delta[i,1]=delta[i-1,1]+deltay[i]
    
    return delta

def main():

    # plots position data from motion capture
    #p.plot(groundtruth[:,1],groundtruth[:,2])

    # plots landmark positions
    p.plot(landmark[:,1],landmark[:,2],'rx')

    delta=odo()

    p.plot(delta[:,0],delta[:,1],'bo')

    p.show()

main()
