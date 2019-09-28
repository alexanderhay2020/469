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


# def dataprep():
#
#     x=np.cos(odometry[:,3])
#     y=np.sin(odometry[:,3])


def main():

    # plots position data from motion capture
    p.plot(groundtruth[:,1],groundtruth[:,2])

    # plots landmark positions
    p.plot(landmark[:,1],landmark[:,2],'rx')

    # plots position data measured from robot
    x=np.cos(measurement[:,3])*measurement[:,2]
    y=np.sin(measurement[:,3])*measurement[:,2]
    #p.plot(x,y)

    p.show()

main()
