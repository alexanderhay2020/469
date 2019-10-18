# Draws Grid

import numpy as np
import pylab as p

# global variables
barcodes = np.loadtxt('ds1_Barcodes.dat')
groundtruth = np.loadtxt('ds1_Groundtruth.dat') # position data from motion capture (may be taken as known information for filtering)
landmark = np.loadtxt('ds1_Landmark_Groundtruth.dat')  # landmark data
measurement = np.loadtxt('ds1_Measurement.dat') # measurement data from robot
odometry = np.loadtxt('ds1_Odometry.dat') # time, forward v, angular v, measured from robot

def plotbarriers(): # displays environment

    # plots graph axes
    p.xlabel("x position (m)")
    p.ylabel("y position (m)")
    p.xlim(-8, 10)
    p.ylim(-7, 7)
    p.autoscale = True

    # plots landmark positions
    p.plot(landmark[:, 1], landmark[:, 2], 'ro')

    # plots barriers
    p.plot([landmark[1, 1], landmark[4, 1]], [landmark[1, 2], landmark[4, 2]], 'k-')  # connects landmarks 7 and 10
    p.plot([landmark[4, 1], landmark[3, 1]], [landmark[4, 2], landmark[3, 2]], 'k-')  # connects landmarks 10 and 9
    p.plot([landmark[3, 1], landmark[0, 1]], [landmark[3, 2], landmark[0, 2]], 'k-')  # connects landmarks 9 and 6
    p.plot([landmark[0, 1], landmark[2, 1]], [landmark[0, 2], landmark[2, 2]], 'k-')  # connects landmarks 6 and 8
    p.plot([landmark[2, 1], landmark[5, 1]], [landmark[2, 2], landmark[5, 2]], 'k-')  # connects landmarks 8 and 11
    p.plot([landmark[5, 1], landmark[6, 1]], [landmark[5, 2], landmark[6, 2]], 'k-')  # connects landmarks 11 and 12
    p.plot([landmark[6, 1], landmark[14, 1]], [landmark[6, 2], landmark[14, 2]], 'k-')  # connects landmarks 12 and 20
    p.plot([landmark[14, 1], landmark[13, 1]], [landmark[14, 2], landmark[13, 2]], 'k-')  # connects landmarks 20 and 19
    p.plot([landmark[13, 1], landmark[12, 1]], [landmark[13, 2], landmark[12, 2]], 'k-')  # connects landmarks 19 and 18
    p.plot([landmark[12, 1], landmark[11, 1]], [landmark[12, 2], landmark[11, 2]], 'k-')  # connects landmarks 18 and 17
    p.plot([landmark[11, 1], landmark[9, 1]], [landmark[11, 2],  landmark[9, 2]], 'k-')  # connects landmarks 17 and 15
    p.plot([landmark[9, 1], landmark[4, 1]], [landmark[9, 2], landmark[4, 2]], 'k-')  # connects landmarks 15 and 10

    # plots island barriers
    p.plot([landmark[10, 1], landmark[8, 1]], [landmark[10, 2], landmark[8, 2]], 'k-')  # connects landmarks 16 and 14
    p.plot([landmark[8, 1], landmark[7, 1]], [landmark[8, 2], landmark[7, 2]], 'k-')  # connects landmarks 14 and 13

    # plots landmark annotations
    for i in range(len(landmark)):
        p.annotate(str(landmark[i, 0])[:-2],  # landmark # label
                   # landmark coordinates for label
                   (landmark[i, 1], landmark[i, 2]),
                   textcoords="offset points",  # how to position text
                   xytext=(7, 10),  # distance from text to points (x,y)
                   ha='center')  # horizontal adjustment; left, right, or center
