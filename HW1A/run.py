"""
Alexander Hay
A* Algorithm

Part A:

1. Build grid cell of 1x1m, ranges x:[-2,5], y:[-6,6].
    * Mark cells with landmarks

2. Implement A* Algorithm

3. Use algorithm to plan paths between the following sets of start/goal positions:

    A: S=[0.5,-1.5], G=[0.5,1.5]
    B: S=[4.5,3.5], G=[4.5-,1.5]
    C: S=[-0.5,5.5], G=[1.5,-3.5]

    * Display occupied cells
    * Display explored cells
    * Display planned path

4. Change program so that robot does not have 'a priori' knowledge of obstacles

5. Repeat step 3 with changes in program

6. Decrease cell size to 0.1x0.1m

    * inflate size of landmarks to be 0.3m circles

7. Use algorithm to plan paths between the following sets of start/goal positions:

        A: S=[2.45,-3.55], G=[0.95,-1.55]
        B: S=[4.95,-0.05], G=[2.45,0.25]
        C: S=[-0.55,1.45], G=[1.95,3.95]

        * Display occupied cells
        * Display explored cells
        * Display planned path
"""

import numpy as np
import matplotlib.pyplot as plt
import math

# global variables
barcodes = np.loadtxt('ds1_Barcodes.dat')
groundtruth = np.loadtxt('ds1_Groundtruth.dat') # position data from motion capture (may be taken as known information for filtering)
landmark = np.loadtxt('ds1_Landmark_Groundtruth.dat')  # landmark data
measurement = np.loadtxt('ds1_Measurement.dat') # measurement data from robot
odometry = np.loadtxt('ds1_Odometry.dat') # time, forward v, angular v, measured from robot

class Node(object):
    """
    creates attributes for each node in grid environment

    self.parent = parent node
    self.position = (x,y)
    self.g = distance from node to start
    self.h = distance from node to goal (heuristic)
    self.f = g + h (cost function)
    """

    def __init__(self, parent=None, position=None):

        self.parent = parent # set of coordinates
        self.position = position # set of coordinates
        self.g = 0
        self.h = 0
        self.f = self.g + self.h

class Grid(object):
    """
    creates environment
    populates environment with landmarks
    + assigns landmark
    """

    def __init__(self, size):
        self.set_cell(size)

    def set_cell(self, size):
        """
        sets grid_map size and node cost
        """
        self.xedges = np.arange(-2,5,size)
        self.yedges = np.arange(-6,6,size)
        self.node_cost = np.ones([len(self.xedges),len(self.yedges)]) # initiaizes each cell cost to be one
        self.landmarks()

    def landmarks(self):
        """
        marks landmarks and their node cost
        """
        inflate = 0.3 # Relevant for Part A #6 of HW1

        for k in range(len(landmark)):
            for i in range(len(self.xedges)): # row index
                # print landmark[k,1]
                # print self.xedges[i]
                if landmark[k,1] >= self.xedges[i] and landmark[k,1] <= self.xedges[i]+1:
                    x = i

            for j in range(len(self.yedges)): # col index
                if landmark[k,2] >= self.yedges[j] and landmark[k,2] <= self.yedges[j]+1:
                    y = j

            self.node_cost[x][y] = 1000 # cost of landmark

            # print str(k) + ": " + str(i) + ", " + str(j)
            # print self.node_cost[i][j]

    def world_to_grid(self, position): # world to grid
        """
        translate world x,y to grid_map i,j
        """
        for i in range(len(self.xedges)): # row index
            if position[0] >= self.xedges[i] and position[0] <= self.xedges[i]+1:
                x = self.xedges[i]

        for j in range(len(self.yedges)): # col index
            if position[1] >= self.yedges[j] and position[1] <= self.yedges[j]+1:
                y = self.yedges[j]

        return (x, y)


    def grid_to_world(self, position): # grid to world
        """
        translate i,j coordinates to x,y world coordinates
        """
        x_coord = []
        y_coord = []
        if hasattr(position[0], "__len__"):
            for i, j in position:
                x_coord.append(self.cell_size * (i + 0.5) - 2)
                y_coord.append(self.cell_size * (j + 0.5) - 6)
            return np.transpose(np.array([x_coord, y_coord]))
        else:
            x_coord.append(self.cell_size * (position[0] + 0.5) - 2)
            y_coord.append(self.cell_size * (position[1] + 0.5) - 6)
            return np.transpose(np.array([x_coord, y_coord]))

class Astar(object):
    """
    A* algorithm
    """
    def __init__(self, start, goal, grid_map):

        # initiatialize costs
        start = grid_map.world_to_grid(start)
        goal = grid_map.world_to_grid(goal)

        start_node = Node(None,start)
        goal_node = Node(None,goal)

        start_node.g = 0 # distance from node to start
        start_node.h = self.heuristic(start_node.position,goal_node.position) # distance from node to goal
        start_node.f = start_node.g + start_node.h

        open_list = [] # all generated nodes
        closed_list = [] # all expanded nodes

        open_list.append(start_node)

        # print "start_node g: " + str(start_node.g)
        # print "start_node h: " + str(start_node.h)
        # print "start_node f: " + str(start_node.f)
        # print start_node.position[1] # prints y since node.postition is (x,y)
        # print "start node"
        # print start_node.position
        # print

        while open_list[0] /= goal_node:
            q = open_list[0] # q is "querrent" (current)

            if q == goal:
                path():

            open_list.pop(0)
            closed_list.append(q)

            child_list = self.children(q, goal_node, grid_map)
            # child = self.children(q, goal_node, grid_map)[0]
            open_list = self.validation(child_list, closed_list, open_list)



    def heuristic(self, position, goal):
        """
        calculates minimum cost from node to goal

        transistion_cost is defined by Grid.node, but I don't know how to access that info, so it's redefined here
        corner_cut returns x difference or y difference (between node and goal), whichever is shorter. because...
        straight_dist returns the opposite, the largest of the x and y differences
        cost = straight_dist + corner_cut (it cuts the corner)
        """
        transition_cost = 1 # defined by Grid.node cost I think but I don't know how to access that information
        corner_cut = min(abs(position[0] - goal[0]), abs(position[1] - goal[1])) # returns x difference or y difference, whichever is shorter
        straight_dist = max(abs(position[0] - goal[0]), abs(position[1] - goal[1]))
        cost = (straight_dist + (math.sqrt(2) * corner_cut)) * transition_cost
        # print "cost: " + str(cost)
        return cost


    def children(self, node, goal, grid_map):
        """
        returns list of possible node children
        """
        child_list = []
        print node.position
        # print goal.position
        index = 0
        for i in range(-1,2):
            for j in range(-1,2):

                position = (node.position[0] + i, node.position[1] + j)
                # index = index + 1
                parent = node
                child = Node(parent=parent, position=position)
                # print "child #: " + str(index)
                # print "child position: " + str(child.position)
                child.g = node.g + child.parent.g
                child.h = self.heuristic(child.position, goal.position)
                # print "child h: " + str(child.h)
                child.f = child.g + child.h

                if child.position == node.position:
                    continue
                #if child.postion == goal.position:
                    #return child
                elif child.position[0] < grid_map.xedges[0] or child.position[0] > grid_map.xedges[-1]:
                    continue
                elif child.position[1] < grid_map.yedges[0] or child.position[1] > grid_map.yedges[-1]:
                    continue
                else:
                    child_list.append(child)

        child_list.sort(key=lambda x: x.f)
        # for i in range(len(child_list)):
        #     print "Child " + str(i) + ": " + str(child_list[i].position)
        #     print child_list[i].f
        #     print

        return child_list

    def validation(child_list, closed_list, open_list):

        for i in range(len(child_list)):

            # checks if child is in closed list
            if (child_list[i] in closed_list):
                for j in range(len(closed_list)):

                    # if child IS in closed list, checks if child.f is greater than closed.f
                    # if it IS greater, child is removed from the child_list
                    if child_list[i].f > closed_list[j].f:
                        child_list.remove(child_list[i])

                    # if child IS in closed list, and if child.f EQUALS closed.f
                    # compares h values
                    # if child.h IS greater, child is removed from child list
                    elif child_list[i].f == closed_list[j].f:
                        if child_list[i].h > closed_list[j].h:
                            child_list.remove(child_list[i])

            # if child IS NOT in closed list
            # checks if child is in open list
            if (child_list[i] in closed_list):
                for k in range(len(open_list)):

                    # if child IS in open list, checks if child.f is greater than open.f
                    # if it IS greater, child is removed from the child_list
                    if child_list[i].f > open_list[k].f:
                        child_list.remove(child_list[i])

                    # if child IS in open list, and if child.f EQUALS open.f
                    # compares h values
                    # if child.h IS greater, child is removed from child list
                elif child_list[i].f == open_list[k].f:
                        if child_list[i].h > open_list[k].h:
                            child_list.remove(child_list[i])

            # if child list passes all that, child is added to open list
            # list is sorted by f
            open_list.append(child_list[i])
            open_list.sort(key=lambda x: x.f)

            return open_list

def plot(grid):
    """
    plots grid_map information
    """

    fig1 = plt.figure()
    plt.imshow(grid.node_cost.T,cmap='plasma',origin='lower',extent=[-2,5,-6,6])
    ax = plt.gca();
    ax.set_xticks(grid.xedges)
    ax.set_yticks(grid.yedges)
    plt.title('Environment')
    plt.xlabel("x position (m)")
    plt.ylabel("y position (m)")
    plt.grid(which='major',axis='both')
    plt.show()

def main():
    """
    text
    """
    grid_map = Grid(1) # CHANGE THIS FOR PART A #6 OF HW1

    start = (0.5,-1.5)
    goal = (0.5,1.5)


    astar = Astar(start, goal, grid_map)
    plot(grid_map)
if __name__ == '__main__':
    main()
