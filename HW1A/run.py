# Draws Grid

import numpy as np
import matplotlib.pyplot as plt

# global variables
barcodes = np.loadtxt('ds1_Barcodes.dat')
groundtruth = np.loadtxt('ds1_Groundtruth.dat') # position data from motion capture (may be taken as known information for filtering)
landmark = np.loadtxt('ds1_Landmark_Groundtruth.dat')  # landmark data
measurement = np.loadtxt('ds1_Measurement.dat') # measurement data from robot
odometry = np.loadtxt('ds1_Odometry.dat') # time, forward v, angular v, measured from robot

class grid():

    def grid(): # displays environment

        xedges = [-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7]
        yedges = [-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7]

        # plots landmark positions
        #plt.plot(landmark[:, 1], landmark[:, 2], 'ro')

        # plots landmark annotations
        # for i in range(len(landmark)):
        #     plt.annotate(str(landmark[i, 0])[:-2],  # landmark # label
        #                # landmark coordinates for label
        #                (landmark[i, 1], landmark[i, 2]),
        #                textcoords="offset points",  # how to position text
        #                xytext=(7, 10),  # distance from text to points (x,y)
        #                ha='center')  # horizontal adjustment; left, right, or center

        # # plots barriers
        # plt.plot([landmark[1,1],landmark[4,1]],[landmark[1,2],landmark[4,2]],'r-') # connects landmarks 7 and 10
        # plt.plot([landmark[4,1],landmark[3,1]],[landmark[4,2],landmark[3,2]],'r-') # connects landmarks 10 and 9
        # plt.plot([landmark[3,1],landmark[0,1]],[landmark[3,2],landmark[0,2]],'r-') # connects landmarks 9 and 6
        # plt.plot([landmark[0,1],landmark[2,1]],[landmark[0,2],landmark[2,2]],'r-') # connects landmarks 6 and 8
        # plt.plot([landmark[2,1],landmark[5,1]],[landmark[2,2],landmark[5,2]],'r-') # connects landmarks 8 and 11
        # plt.plot([landmark[5,1],landmark[6,1]],[landmark[5,2],landmark[6,2]],'r-') # connects landmarks 11 and 12
        # plt.plot([landmark[6,1],landmark[14,1]],[landmark[6,2],landmark[14,2]],'r-') # connects landmarks 12 and 20
        # plt.plot([landmark[14,1],landmark[13,1]],[landmark[14,2],landmark[13,2]],'r-') # connects landmarks 20 and 19
        # plt.plot([landmark[13,1],landmark[12,1]],[landmark[13,2],landmark[12,2]],'r-') # connects landmarks 19 and 18
        # plt.plot([landmark[12,1],landmark[11,1]],[landmark[12,2],landmark[11,2]],'r-') # connects landmarks 18 and 17
        # plt.plot([landmark[11,1],landmark[9,1]],[landmark[11,2],landmark[9,2]],'r-') # connects landmarks 17 and 15
        # plt.plot([landmark[9,1],landmark[4,1]],[landmark[9,2],landmark[4,2]],'r-') # connects landmarks 15 and 10
        #
        # # plots island barriers
        # plt.plot([landmark[10,1],landmark[8,1]],[landmark[10,2],landmark[8,2]],'r-') # connects landmarks 16 and 14
        # plt.plot([landmark[8,1],landmark[7,1]],[landmark[8,2],landmark[7,2]],'r-') # connects landmarks 14 and 13


        # H = H.T  # Let each row list bins with common y range.
        fig2 = plt.figure()
        # # plots barriers
        plt.plot([landmark[1,1],landmark[4,1]],[landmark[1,2],landmark[4,2]],'r-') # connects landmarks 7 and 10
        plt.plot([landmark[4,1],landmark[3,1]],[landmark[4,2],landmark[3,2]],'r-') # connects landmarks 10 and 9
        plt.plot([landmark[3,1],landmark[0,1]],[landmark[3,2],landmark[0,2]],'r-') # connects landmarks 9 and 6
        plt.plot([landmark[0,1],landmark[2,1]],[landmark[0,2],landmark[2,2]],'r-') # connects landmarks 6 and 8
        plt.plot([landmark[2,1],landmark[5,1]],[landmark[2,2],landmark[5,2]],'r-') # connects landmarks 8 and 11
        plt.plot([landmark[fig2 = plt.figure(5,1],landmark[6,1]],[landmark[5,2],landmark[6,2]],'r-') # connects landmarks 11 and 12
        plt.plot([landmark[6,1],landmark[14,1]],[landmark[6,2],landmark[14,2]],'r-') # connects landmarks 12 and 20
        plt.plot([landmark[14,1],landmark[13,1]],[landmark[14,2],landmark[13,2]],'r-') # connects landmarks 20 and 19
        plt.plot([landmark[13,1],landmark[12,1]],[landmark[13,2],landmark[12,2]],'r-') # connects landmarks 19 and 18
        plt.plot([landmark[12,1],landmark[11,1]],[landmark[12,2],landmark[11,2]],'r-') # connects landmarks 18 and 17
        plt.plot([landmark[11,1],landmark[9,1]],[landmark[11,2],landmark[9,2]],'r-') # connects landmarks 17 and 15
        plt.plot([landmark[9,1],landmark[4,1]],[landmark[9,2],landmark[4,2]],'r-') # connects landmarks 15 and 10

        # plots island barriers
        plt.plot([landmark[10,1],landmark[8,1]],[landmark[10,2],landmark[8,2]],'r-') # connects landmarks 16 and 14
        plt.plot([landmark[8,1],landmark[7,1]],[landmark[8,2],landmark[7,2]],'r-') # connects landmarks 14 and 13
        plt.hist2d(landmark[:, 1], landmark[:, 2], bins=(xedges, yedges), cmap=plt.cm.BuGn_r)
        plt.title('Histogram')
        plt.xticks(xedges)
        plt.yticks(yedges)
        plt.xlabel("x position (m)")
        plt.ylabel("y position (m)")
        # plt.xlim(-2,5)
        # plt.ylim(-6,6)
        plt.grid()
        plt.show()

    grid()

grid()

# #class grid():
#
#     """
#     This is the grid class
#
#     """
#
#     def __init__(grid,coor,flag,start,goal):
#
#         grid = np.zeros((12,12))
#         for i in range(len(grid)):
#             grid[i] = np.arange(i,i+1,0.1)
#
#
#         # need to map index to grid space
#         grid.flag = flag # occupied, unoccupied
#         grid.coor.x = x
#         grid.coor.y = y
