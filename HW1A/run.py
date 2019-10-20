# Draws grid_map

import numpy as np
import matplotlib.pyplot as plt


# global variables
barcodes = np.loadtxt('ds1_Barcodes.dat')
groundtruth = np.loadtxt('ds1_Groundtruth.dat') # position data from motion capture (may be taken as known information for filtering)
landmark = np.loadtxt('ds1_Landmark_Groundtruth.dat')  # landmark data
measurement = np.loadtxt('ds1_Measurement.dat') # measurement data from robot
odometry = np.loadtxt('ds1_Odometry.dat') # time, forward v, angular v, measured from robot

#class grid_map():

def __init__(self,cell_size_landmarks):
    self.attribute1 = whatever
    self.attribute2 = whatever

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

    return grid_map

class Node():
    """
    Keeps track of nodes attributes
    """

    def __init__(self,parent,pos,start=None,goal=None):

        self.parent = parent
        self.x = pos[0]
        self.y = pos[1]

        self.g = 0 # cost to node
        self.h = 0 # cost to goal (heuristic)
        self.f = 0 # g + h

    def children(grid,cell):
        # if parent:
        #     self.path = parent.path[:]
        #     self.path.append(f)
        #     self.start = parent.start
        #     self.goal = parent.goal
        # else:
        #     self.path = f
        #     self.start = start
        #     self.goal = goal

    def estimate(self, dx, dy):

        x = dx - self.x
        y = dy - self.y

        # Euclidian Distance
        # d = math.sqrt(xd * xd + yd * yd)
        # Manhattan distance
        d = abs(xd) + abs(yd)

        return(d)


def a_star(grid_map,start,goal):

    start_node = Node(None,start)
    start_node.g = 0
    start_node.h = 0
    start_node.f = start_node.g + start_node.h

    goal_node = Node(None,goal)
    goal_node.g = 0
    goal_node.h = 0
    goal_node.f = goal_node.g + goal_node.h

    # initialize lists
    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0

        current_node = open_list[0]
        i = 0
        open_list.remove(current_node)
        closed_list.append(current_node)

        if current_node == goal_node:
            break

        for n in

def plotter(grid):
    # # plots barriers
    # plt.plot([landmark[1,1],landmark[4,1]],[landmark[1,2],landmark[4,2]],'k-') # connects landmarks 7 and 10
    # plt.plot([landmark[4,1],landmark[3,1]],[landmark[4,2],landmark[3,2]],'k-') # connects landmarks 10 and 9
    # plt.plot([landmark[3,1],landmark[0,1]],[landmark[3,2],landmark[0,2]],'k-') # connects landmarks 9 and 6
    # plt.plot([landmark[0,1],landmark[2,1]],[landmark[0,2],landmark[2,2]],'k-') # connects landmarks 6 and 8
    # plt.plot([landmark[2,1],landmark[5,1]],[landmark[2,2],landmark[5,2]],'k-') # connects landmarks 8 and 11
    # plt.plot([landmark[5,1],landmark[6,1]],[landmark[5,2],landmark[6,2]],'k-') # connects landmarks 11 and 12
    # plt.plot([landmark[6,1],landmark[14,1]],[landmark[6,2],landmark[14,2]],'k-') # connects landmarks 12 and 20
    # plt.plot([landmark[14,1],landmark[13,1]],[landmark[14,2],landmark[13,2]],'k-') # connects landmarks 20 and 19
    # plt.plot([landmark[13,1],landmark[12,1]],[landmark[13,2],landmark[12,2]],'k-') # connects landmarks 19 and 18
    # plt.plot([landmark[12,1],landmark[11,1]],[landmark[12,2],landmark[11,2]],'k-') # connects landmarks 18 and 17
    # plt.plot([landmark[11,1],landmark[9,1]],[landmark[11,2],landmark[9,2]],'k-') # connects landmarks 17 and 15
    # plt.plot([landmark[9,1],landmark[4,1]],[landmark[9,2],landmark[4,2]],'k-') # connects landmarks 15 and 10
    #
    # # plots island barriers
    # plt.plot([landmark[10,1],landmark[8,1]],[landmark[10,2],landmark[8,2]],'k-') # connects landmarks 16 and 14
    # plt.plot([landmark[8,1],landmark[7,1]],[landmark[8,2],landmark[7,2]],'k-') # connects landmarks 14 and 13
    #
    # for i in range(len(landmark)):
    #     plt.annotate(str(landmark[i, 0])[:-2],  # landmark # label
    #                # landmark coordinates for label
    #                (landmark[i, 1], landmark[i, 2]),
    #                textcoords="offset points",  # how to position text
    #                xytext=(7, 10),  # distance from text to points (x,y)
    #                ha='center')  # horizontal adjustment; left, right, or center
    # displays environment
    xedges = [-2,-1,0,1,2,3,4]
    yedges = [-6,-5,-4,-3,-2,-1,0,1,2,3,4,5]

    x_lo_extent = xedges[0]
    x_hi_extent = xedges[-1]
    y_lo_extent = yedges[0]
    y_hi_extent = yedges[-1]

    fig1 = plt.figure()
    plt.imshow(grid.T,cmap='plasma',origin='lower',extent=[-2,4,-6,5])
    ax = plt.gca();
    ax.set_xticks(xedges)
    ax.set_yticks(yedges)
    plt.title('Environment')
    plt.xlabel("x position (m)")
    plt.ylabel("y position (m)")
    plt.grid(which='major',axis='both')
    plt.show()

def main():

    map = grid_map()
    plotter(map)

main()
