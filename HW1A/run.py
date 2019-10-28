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

    Parameters:
    parent --- tuple (x,y) of parent node, starting node has no parent
    position - tuple (x,y) of itself

    Attributes:
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
    sets grid_map size and node cost

    Parameters:
    node size ----- float of the size of the node in meters
    start --------- tuple (x,y) of start node
    goal ---------- tuple (x,y) of goal node

    Attributes:
    start --------- starting node in grid coordinates
    goal ---------- goal node in grid coordinates
    landmark_list - list of landmarks (used for debugging)
    xedges -------- an array of the x coordinates for nodes the grid_map is built of
    yedges -------- an array of the y coordinates for nodes the grid_map is built of
    node_cost ----- the cost of entering that node

    Functions:
    set_node ------ determines how many nodes to populate world with and their size
    landmarks ----- converts landmark point to a node, sets node_cost of landmark node to 1000
    world_to_grid - converts world points to their nodes points
    """

    def __init__(self, size, start, goal):
        # self.landmark_list = []
        self.set_node(size)
        self.start=self.world_to_grid(start)
        self.goal=self.world_to_grid(goal)


    def set_node(self, size):
        """
        determines how many nodes to populate world with and their size
        """

        self.xedges = np.arange(-2,5,size)
        self.yedges = np.arange(-6,6,size)
        self.node_cost = np.ones([len(self.xedges),len(self.yedges)]) # initiaizes each cell cost to be one
        self.landmarks()

    def landmarks(self):
        """
        defines landmarks and their node cost
        """
        inflate = 0.3 # Relevant for Part A #6 of HW1

        for k in range(len(landmark)):
            for i in range(len(self.xedges)): # row index
                if landmark[k,1] >= self.xedges[i] and landmark[k,1] <= self.xedges[i]+1:
                    x = i

            for j in range(len(self.yedges)): # col index
                if landmark[k,2] >= self.yedges[j] and landmark[k,2] <= self.yedges[j]+1:
                    y = j
            self.node_cost[x][y] = 1000 # cost of landmark

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

class Astar(object): #start, goal, grid_map):
    """
    A* algorithm

    Parameters:
    start ------ raw start location
    goal ------- raw goal location
    grid_map --- map created by Grid class

    Attributes:
    start ------ start location relative to the grip map
    goal ------- goal location relative to the grip map

    Fuctions:
    heuristic -- calculates the minimum cost from node location to goal
    children --- returns a list of potential node children
    validation - vets children against open and closed lists with their f and h values, returns updated open list sorted by f values
    """
    def __init__(self, start, goal, grid_map):

        # initiatialize costs
        self.start = grid_map.world_to_grid(start)
        self.goal = grid_map.world_to_grid(goal)
        # print self.goal
        start_node = Node(None,self.start)
        goal_node = Node(None,self.goal)

        start_node.g = 0 # distance from node to start
        start_node.h = self.heuristic(start_node.position,goal_node.position) # distance from node to goal
        start_node.f = start_node.g + start_node.h # cost function

        open_list = [] # all generated nodes
        closed_list = [] # all expanded nodes

        open_list.append(start_node)

        while open_list[0] != goal_node:

            q = open_list[0]

            if q.position == goal_node.position:
                path = []
                trace = q
                while trace is not None:
                    path.append(trace.position)
                    trace = trace.parent
                self.path=path
                return #path

            open_list.pop(0)
            closed_list.append(q)

            child_list = self.children(q, goal_node, grid_map)
            open_list = self.validation(child_list, closed_list, open_list)

    def heuristic(self, position, goal):
        """
        calculates minimum cost from node to goal

        transistion_cost is defined by Grid.node, but I don't know how to access that info, so it's redefined here
        hypotenuse is the straight line distance to goal

        cost is the hypotenuse times the transition cost
        """
        transition_cost = 1 #grid.node_cost this should be defined by Grid.node cost I think but I don't know how to access that information
        hypotenuse = math.sqrt((position[0] - goal[0])**2 + (position[1] - goal[1])**2)
        cost = hypotenuse * transition_cost
        # corner_cut = min(abs(position[0] - goal[0]), abs(position[1] - goal[1])) # returns x difference or y difference, whichever is shorter
        # straight_dist = max(abs(position[0] - goal[0]), abs(position[1] - goal[1]))
        # cost = (straight_dist + corner_cut) * transition_cost # cutting corners does not affect cost. moving diagonal=1, moving udlr=1
        # # print "cost: " + str(cost)
        return cost

    def children(self, node, goal, grid_map):
        """
        returns list of possible node children
        """
        child_list = []

        index = 0
        for i in range(-1,2):
            for j in range(-1,2):

                position = (node.position[0] + i, node.position[1] + j)
                # index = index + 1
                parent = node
                child = Node(parent=parent, position=position)
                # print "child #: " + str(index)
                # print "child position: " + str(child.position)

                # print position
                # print grid_map.node_cost
                child.g = grid_map.node_cost[position[0]][position[1]] + child.parent.g
                child.h = self.heuristic(child.position, goal.position)
                child.f = child.g + child.h

                if child.position == node.position:
                    continue
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

    def validation(self, child_list, closed_list, open_list):

        for i in range(len(child_list)):

            # checks if child is in closed list
            if (child_list[i] in closed_list):
                for j in range(len(closed_list)):

                    # if child IS in closed list, checks if child.f is greater than closed.f
                    # if it IS greater, child is removed from the child_list
                    if child_list[i].f > closed_list[j].f:
                        # print yes
                        child_list.remove(child_list[i])

                    # if child IS in closed list, and if child.f EQUALS closed.f
                    # compares h values
                    # if child.h IS greater, child is removed from child list
                    elif child_list[i].f == closed_list[j].f:
                        if child_list[i].h > closed_list[j].h:
                            child_list.remove(child_list[i])

            # if child IS NOT in closed list
            # checks if child is in open list
            if (child_list[i] in open_list):
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
            # a = open_list[0]
            # print a.position
            # print a.h
            # print

            return open_list


class Astar_online(object): #start, goal, grid_map):
    """
    A* algorithm

    Parameters:
    start ------ raw start location
    goal ------- raw goal location
    grid_map --- map created by Grid class

    Attributes:
    start ------ start location relative to the grip map
    goal ------- goal location relative to the grip map

    Fuctions:
    heuristic -- calculates the minimum cost from node location to goal
    children --- returns a list of potential node children
    """
    def __init__(self, start, goal, grid_map):

        # initiatialize costs
        self.start = grid_map.world_to_grid(start)
        self.goal = grid_map.world_to_grid(goal)

        start_node = Node(None,self.start)
        goal_node = Node(None,self.goal)

        start_node.g = 0 # distance from node to start
        start_node.h = self.heuristic(start_node.position,goal_node.position) # distance from node to goal
        start_node.f = start_node.g + start_node.h

        open_list = [] # all generated nodes

        open_list.append(start_node)

        while open_list != goal_node:

            q = open_list[0]

            if q.position == goal_node.position:
                path = []
                trace = q
                while trace is not None:
                    path.append(trace.position)
                    trace = trace.parent
                self.path=path
                return #path

            open_list.pop(0)

            child_list = self.children(q, goal_node, grid_map)
            open_list = child_list

    def heuristic(self, position, goal):
        """
        calculates minimum cost from node to goal

        transistion_cost is defined by Grid.node, but I don't know how to access that info, so it's redefined here
        hypotenuse is the straight line distance to goal
        cost is the hypotenuse times the transition cost
        """
        transition_cost = 1 #grid.node_cost this should be defined by Grid.node cost I think but I don't know how to access that information
        hypotenuse = math.sqrt((position[0] - goal[0])**2 + (position[1] - goal[1])**2)
        cost = hypotenuse * transition_cost
        # # print "cost: " + str(cost)
        return cost

    def children(self, node, goal, grid_map):
        """
        returns list of possible node children
        """
        child_list = []

        index = 0
        for i in range(-1,2):
            for j in range(-1,2):

                position = (node.position[0] + i, node.position[1] + j)
                # index = index + 1
                parent = node
                child = Node(parent=parent, position=position)
                # print "child #: " + str(index)
                # print "child position: " + str(child.position)
                child.g = grid_map.node_cost[position[0]][position[1]] + child.parent.g
                child.h = self.heuristic(child.position, goal.position)
                child.f = child.g + child.h

                if child.position == node.position:
                    continue
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

def plot(grid,path,start,goal,num,method):
    """
    plots grid_map information
    """

    plt.imshow(grid.node_cost.T,origin='lower',extent=[-2,5,-6,6])
    plt.plot(grid.start[0],grid.start[1],'go',label="Start Node")
    plt.plot(grid.goal[0],grid.goal[1],'bo',label="Goal Node")

    for i in range(len(path)):
        dot = path[i]
        plt.plot(dot[0],dot[1],'rx',label="Route")

    ax = plt.gca();
    ax.set_xticks(grid.xedges)
    ax.set_yticks(grid.yedges)

    plt.title('Figure ' + str(num) + ", " + method)
    plt.xlabel("x position (m)")
    plt.ylabel("y position (m)")
    plt.grid(which='major',axis='both')
    ax.legend()
    plt.show()

def main():
    """
    executes the assignment

    Fuctions:
    do_hw - automates inputs and parameters for hw questions.
    """
    start_list1 = [(0.5,-1.5),(4.5,3.5),(-0.5,5.5)]
    goal_list1 = [(0.5,1.5),(4.5,-1.5),(1.5,-3.5)]
    start_list2 = [(2.45,-3.55),(4.95,-0.05),(-0.55,1.45)]
    goal_list2 = [(0.95,-1.55),(2.45,0.25),(1.95,3.95)]

    def do_hw(start,goal,i,method,size):
        """
        Automates HW

        Parameters:
        start -- start location defined by hw problem
        goal --- goal location defined by hw problem
        i ------ iterator for figures
        method - runs the algorithm offline or online, defined by hw problem
        size --- sets the node size, defined by hw problem
        """
        print "Set " + str(i) + ": "
        if method == "Offline":
            grid_map = Grid(size,start,goal)
            astar = Astar(start, goal, grid_map)
            print "Start Node: " + str(start)
            print "Goal Node: " + str(goal)
            print "Path: " + str(astar.path)
            plot(grid_map,astar.path,start,goal,i,method)

        elif method == "Online":
            grid_map = Grid(size,start,goal)
            astar = Astar_online(start, goal, grid_map)
            print "Start Node: " + str(start)
            print "Goal Node: " + str(goal)
            print "Path: " + str(astar.path)
            plot(grid_map,astar.path,start,goal,i+3,method)
        print

    print "Part A, #3"
    for i in range(3):
        do_hw(start_list1[i],goal_list1[i],i+1,"Offline",1)
    print

    print "Part A, #5"
    for i in range(3):
        do_hw(start_list1[i],goal_list1[i],i+1,"Online",1)
    print

    # print "Part A, #7"
    # for i in range(3):
    #     do_hw(start_list2[i],goal_list2[i],i+1,"Offline",10)
    # print

    print "Part A, #7*"
    for i in range(2):
        do_hw(start_list2[i],goal_list2[i],i+7,"Offline",1)

if __name__ == '__main__':
    main()
