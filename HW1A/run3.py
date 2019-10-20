"""
text
"""

import numpy as np
import matplotlib.pyplot as plt

# global variables
barcodes = np.loadtxt('ds1_Barcodes.dat')
groundtruth = np.loadtxt('ds1_Groundtruth.dat') # position data from motion capture (may be taken as known information for filtering)
landmark = np.loadtxt('ds1_Landmark_Groundtruth.dat')  # landmark data
measurement = np.loadtxt('ds1_Measurement.dat') # measurement data from robot
odometry = np.loadtxt('ds1_Odometry.dat') # time, forward v, angular v, measured from robot

class Node():
    """
    text
    """
    
    self.g = 0 # cost to node
    self.h = 0 # cost to goal (heuristic)

class a_star():
    """
    text
    """
    def grid_map(): # creates environment

        xedges = [-2,-1,0,1,2,3,4]
        yedges = [-6,-5,-4,-3,-2,-1,0,1,2,3,4,5]

        grid_map = np.zeros(([len(xedges),len(yedges)]))

        for k in range(len(landmark)):
            for i in range(len(xedges)): # row index
                if landmark[k,1] >= xedges[i] and landmark[k,1] <= xedges[i]+1:
                    x = i

            for j in range(len(yedges)): # col index
                if landmark[k,2] >= yedges[j] and landmark[k,2] <= yedges[j]+1:
                    y = j

            grid_map[x,y] = 100
            #print str(x) + ", " + str(y)
        return grid_map

    def path(start,goal): # {vector3, vector3}
        """
        text
        """
        start_node = start
        open_list = []
        closed_list = []

        open_set.append(start_node)

        while len(open_list) > 0:
