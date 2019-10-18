# Draws Grid

import numpy as np
import matplotlib.pyplot as plt

# global variables
barcodes = np.loadtxt('ds1_Barcodes.dat')
groundtruth = np.loadtxt('ds1_Groundtruth.dat') # position data from motion capture (may be taken as known information for filtering)
landmark = np.loadtxt('ds1_Landmark_Groundtruth.dat')  # landmark data
measurement = np.loadtxt('ds1_Measurement.dat') # measurement data from robot
odometry = np.loadtxt('ds1_Odometry.dat') # time, forward v, angular v, measured from robot

def grid(): # displays environment

    # plots graph axes
    plt.xlabel("x position (m)")
    plt.ylabel("y position (m)")
    plt.xlim(-2,5)
    plt.ylim(-6,6)
    plt.autoscale = True

    # plots landmark positions
    plt.plot(landmark[:, 1], landmark[:, 2], 'ro')

    # plots landmark annotations
    # for i in range(len(landmark)):
    #     plt.annotate(str(landmark[i, 0])[:-2],  # landmark # label
    #                # landmark coordinates for label
    #                (landmark[i, 1], landmark[i, 2]),
    #                textcoords="offset points",  # how to position text
    #                xytext=(7, 10),  # distance from text to points (x,y)
    #                ha='center')  # horizontal adjustment; left, right, or center


    xedges = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
    yedges = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]

    # x = np.zeros(100)
    # y = np.zeros(100)
    # H, xedges, yedges = np.histogram2d(x, y, bins=(xedges, yedges))
    # H = H.T  # Let each row list bins with common y range.

    plt.hist2d(landmark[:, 1], landmark[:, 2], bins=(xedges, yedges), cmap=plt.cm.BuGn_r)
    fig = plt.figure(figsize=(5, 5))
    #ax = fig.add_subplot(title='imshow: square bins')
    # plt.imshow(H, interpolation='nearest', origin='low',
    #        extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]])
    plt.grid()
    plt.show()

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