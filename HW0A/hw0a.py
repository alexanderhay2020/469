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

def odo():

    # 2D array to hold calculated x, y, and theta values
    delta=np.zeros((len(odometry),3))

    delta[0,0]=initialx
    delta[0,1]=initialy
    delta[0,2]=initialrad

    # calulates time and theta, then applies displacement equations
    for i in range(1,len(odometry)-1):

        time=odometry[i+1,0]-odometry[i,0] # executes command from timestamp until next command is issued
        vel=odometry[i,1]

        delta[i,2]=delta[i-1,2]+(odometry[i,2]*time) # theta value
        delta[i,0]=delta[i-1,0]+vel*np.cos(delta[i,2])*time # finds x displacement (m) x=v*cos(theta)*t
        delta[i,1]=delta[i-1,1]+vel*np.sin(delta[i,2])*time # finds y displacement (m) x=v*sin(theta)*t

        # xt is the state vector
        # At is an nxn identity matrix
        # B is an mxm matrix
        # ut is the control vector
        # zt is the sensor vector
        # Et is state transition noise
        # dt is measurement noise

        xt=delta[i,:]
        ut=[vel*np.cos(delta[i,2]),vel*np.sin(delta[i,2]),odometry[i,2]]
        ut=np.asarray(ut) # converts list to array for posterity
        At=np.identity(len(xt))

        B=np.zeros((len(xt),len(xt))) # creates change in time matrix
        np.fill_diagonal(B,[time])

    return delta

def plotbarriers():

    # plots graph title and axes
    p.title("Global Position")
    p.xlabel("x position (m)")
    p.ylabel("y position (m)")
    p.autoscale=True

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

def main():

    delta=odo()
    plotbarriers()
    # plots position data from motion capture
    p.plot(groundtruth[:,1],groundtruth[:,2],'b-',label='groundtruth')
    p.plot(delta[:,0],delta[:,1],'g-',label='odometry')

    # creates legend
    p.legend(loc='best')

    p.show()

main()
