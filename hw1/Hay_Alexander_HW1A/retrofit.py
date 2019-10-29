"""
Alexander Hay

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
    Node class, keeps track of parent and position
    """

    def __init__(self, parent=None, position=None):

        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def astar(maze, start, end):
    """
    Returns path coordinates from start to finish

    This section is code copied from https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
    in trying to understand the child node aspect
    """

    # Create start and end node and their costs
    start_node = Node(None, start)
    start_node.g = 0
    start_node.h = 0
    start_node.f = start_node.g + start_node.h

    end_node = Node(None, end)
    end_node.g = 0
    end_node.h = 0
    end_node.f = end_node.g + end_node.h

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop through open list
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Remove current from open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within boundary
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure position is valid
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)

def grid_map():
    """
    creates environment
    """
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

def plotter(grid,path):
    """
    text
    """
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
    #plt.plot(xyland[:, 0], xyland[:, 1], 'rx', label='landmark position')
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

    start = (4.5,3.5)
    end = (4.5,-1.5)
    plotter(map,None)
    path = astar(map, start, end)
    print(path)
    #plotter(map,path)

if __name__ == '__main__':
    main()
