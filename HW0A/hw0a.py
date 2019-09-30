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

    # 4D array to hold calculated displacement, theta, x, and Y values
    delta=np.zeros((len(odometry),4))

    delta[0,2]=initialx
    delta[0,3]=initialy

    # calulates mometary displacement and theta
    for i in range(len(odometry)):
        if i==0:
            delta[i,0]=odometry[i,1]*(odometry[i,0]-initialt) # finds displacement (m)
            delta[i,1]=odometry[i,2]*(odometry[i,0]-initialt) # finds delta theta (rad)

        else:
            delta[i,0]=odometry[i,1]*(odometry[i,0]-odometry[i-1,0]) # finds displacement (m)
            delta[i,1]=odometry[i,2]*(odometry[i,0]-odometry[i-1,0]) # finds delta theta (rad)

    # translates displacement into x & y coordinates

    for i in range(len(delta)):
        if i==0:
            delta[i,2]=np.cos(delta[i,1]-initialrad)*delta[i,0]
            delta[i,3]=np.sin(delta[i,1]-initialrad)*delta[i,0]
        else:
            delta[i,2]=np.cos(delta[i,1]+delta[i-1,1])*delta[i,0]
            delta[i,3]=np.sin(delta[i,1]+delta[i-1,1])*delta[i,0]

    for i in range(1,len(delta)):
        delta[i,2]=delta[i-1,2]+delta[i,2]
        delta[i,3]=delta[i-1,3]+delta[i,3]

    return delta

def plotbarriers():

    # plots graph title and axes
    p.title("Global Position")
    p.xlabel("x position (m)")
    p.ylabel("y position (m)")

    # plots landmark positions
    p.plot(landmark[:,1],landmark[:,2],'ro')

    # plots barriers
    p.plot([landmark[1,1],landmark[4,1]],[landmark[1,2],landmark[4,2]],'k-') # connects landmarks 7 and 10
    p.plot([landmark[4,1],landmark[3,1]],[landmark[4,2],landmark[3,2]],'k-') # connects landmarks 10 and 9
    p.plot([landmark[3,1],landmark[0,1]],[landmark[3,2],landmark[0,2]],'k-') # connects landmarks 9 and 6
    p.plot([landmark[0,1],landmark[2,1]],[landmark[0,2],landmark[2,2]],'k-') # connects landmarks 6 and 8
    p.plot([landmark[2,1],landmark[5,1]],[landmark[2,2],landmark[5,2]],'k-') # connects landmarks 8 and 11
    p.plot([landmark[5,1],landmark[6,1]],[landmark[5,2],landmark[6,2]],'k-') # connects landmarks 11 and 12
    p.plot([landmark[6,1],landmark[14,1]],[landmark[6,2],landmark[14,2]],'k-') # connects landmarks 12 and 20
    p.plot([landmark[14,1],landmark[13,1]],[landmark[14,2],landmark[13,2]],'k-') # connects landmarks 20 and 19
    p.plot([landmark[13,1],landmark[12,1]],[landmark[13,2],landmark[12,2]],'k-') # connects landmarks 19 and 18
    p.plot([landmark[12,1],landmark[11,1]],[landmark[12,2],landmark[11,2]],'k-') # connects landmarks 18 and 17
    p.plot([landmark[11,1],landmark[9,1]],[landmark[11,2],landmark[9,2]],'k-') # connects landmarks 17 and 15
    p.plot([landmark[9,1],landmark[4,1]],[landmark[9,2],landmark[4,2]],'k-') # connects landmarks 15 and 10

    p.plot([landmark[10,1],landmark[8,1]],[landmark[10,2],landmark[8,2]],'k-') # connects landmarks 16 and 14
    p.plot([landmark[8,1],landmark[7,1]],[landmark[8,2],landmark[7,2]],'k-') # connects landmarks 14 and 13

    # plots landmark annotations
    for i in range(len(landmark)):
        p.annotate(str(landmark[i,0])[:-2], # landmark # label
        (landmark[i,1],landmark[i,2]), # landmark coordinates for label
        textcoords="offset points", # how to position text
        xytext=(7,10), # distance from text to points (x,y)
        ha='center') # horizontal adjustment; left, right, or center

    # plots position data from motion capture
    p.plot(groundtruth[:,1],groundtruth[:,2],'b-',label='groundtruth')

    # creates legend
    p.legend(loc='best')

def main():

    delta=odo()
    plotbarriers()
    #p.plot(delta[:,2],delta[:,3],'bo')

    p.show()

main()
