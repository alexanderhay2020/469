# Alexander Hay
# ME_469, HW0, Part A3
# Dataset 1, Particle Filter
# Applied Motion Model

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
    xt=np.zeros((len(odometry),3))
    zt=np.zeros((len(odometry),3))

    delta[0,0]=initialx
    delta[0,1]=initialy
    delta[0,2]=initialrad

    for i in range(1,len(odometry)-1):

        # ************************************
        # This section calculates robot's position
        # from odometry data

        time=odometry[i+1,0]-odometry[i,0] # executes command from timestamp until next command is issued
        vel=odometry[i,1]

        delta[i,2]=delta[i-1,2]+(odometry[i,2]*time) # theta value in rad
        delta[i,0]=delta[i-1,0]+vel*np.cos(delta[i,2])*time # finds x displacement (m) x=v*cos(theta)*t
        delta[i,1]=delta[i-1,1]+vel*np.sin(delta[i,2])*time # finds y displacement (m) x=v*sin(theta)*t

        #**************************************
        # this section predicts robot's position
        # this section also needs work. I struggled to apply the vector math correctly
        # it could just be a plotting error

        # xt - the state vector
        # At - nxn identity matrix
        # B  - mxm matrix
        # ut - control vector
        # zt - the sensor vector
        # Et - state transition noise, will also be used for measurement model in place of (dt)

        xtvector=delta[i-1,:]
        xtvector=xtvector.reshape(-1,1) # row vector to column vector
        ut=[vel*np.cos(delta[i,2]),vel*np.sin(delta[i,2]),odometry[i,2]]
        ut=np.asarray(ut) # converts list to array for posterity
        ut=ut.reshape(-1,1) # row to column vector
        At=np.identity(len(xtvector))

        B=np.zeros((len(xtvector),len(xtvector))) # creates change in time matrix
        np.fill_diagonal(B,[time])

        covar=1 # chosen because standard normal distribution, sigma =1, 1^2=1

        Et=np.matrix([[np.random.normal(0,covar)],[np.random.normal(0,covar)],[np.random.normal(0,covar)]])
        # standard normal distributionfor noise

        xtvector=(np.matmul(At,xtvector)+np.matmul(B,ut))+Et
        xt[i]=xtvector.reshape(1,-1)
        probxt=np.random.normal(xtvector,covar)

        #probzt=np.random.normal(ztvector,covar)

    return [delta,xt]

def plotbarriers():

    # plots graph axes
    p.xlabel("x position (m)")
    p.ylabel("y position (m)")
    p.xlim(-8,10)
    p.ylim(-7,7)
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

    # plots island barriers
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

    paths=odo()
    delta=paths[0]
    hot_trash=paths[1]
    plotbarriers()
    p.title("Robot Odometry vs Ground Truth")
    p.plot(delta[:,0],delta[:,1],'b-',label='Robot Odometry') # plots position data derived from odometry readings
    p.plot(groundtruth[:,1],groundtruth[:,2],'g-',label='Ground Truth') # plots position data from motion capture
    p.legend(loc='best')
    plt.figure()
    plotbarriers()
    p.title("Robot Odometry vs Dead-Reckoning")
    p.plot(delta[:,0],delta[:,1],'b-',label='Robot Odometry') # plots position data derived from odometry readings
    p.plot(hot_trash[:100,0],hot_trash[:100,1],'r-',label='Dead-Reckoning') # plots position data estimate
    p.legend(loc='best')

    p.show()

main()
