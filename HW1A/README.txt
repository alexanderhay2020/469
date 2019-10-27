# ME 469 - Homework 1B

Alexander Hay
ME 469, HW1, Part B
A* Search and Navigation

---------------------------------
Code Breakdown

  Imports and Global Variables:

    Imports:
    + numpy
    + matplotlib
    + math

    Global Variables:
    + barcodes ----- ds1_Barcodes.dat
    + groundtruth -- ds1_Groundtruth.dat
    + landmark ----- ds1_Landmark_Groundtruth.dat
    + measurement -- ds1_Measurement.dat
    + odometry ----- ds1_Odometry.dat

  Classes and Functions

    Node (Class)
    Defines attributes for each node

      Parameters:
      + parent --- tuple (x,y) of parent node, starting node has no parent
      + position - tuple (x,y) of itself

      Attributes:
      + parent --- parent node
      + position - (x,y)
      + g -------- distance from node to start
      + h -------- distance from node to goal (heuristic)
      + f -------- g + h (cost function)


    Grid (Class)
    Sets grid_map node size and node cost

      Parameters:
      + node size - float of the size of the node in meters
      + start ----- tuple (x,y) of start node
      + goal ------ tuple (x,y) of goal node

      Attributes:
      + goal ---------- goal node in grid coordinates
      + start --------- starting node in grid coordinates
      + landmark_list - list of landmarks (used for debugging)
      + xedges -------- an array of the x coordinates for nodes the grid_map is built of
      + yedges -------- an array of the y coordinates for nodes the grid_map is built of
      + node_cost ----- the cost of entering that node

      Functions:
      + set_cell ------ determines how many nodes to populate world with and their size
      + landmarks ----- converts landmark point to a node, sets node_cost of landmark node to 1000
      + world_to_grid - converts world points to their nodes points


    Astar (Class)
    A* algorithm

      Parameters:
      + start ---- raw start location
      + goal ----- raw goal location
      + grid_map - map created by Grid class

      Attributes:
      + start - start location relative to the grip map
      + goal -- goal location relative to the grip

      Functions:
      + heuristic -- calculates the minimum cost from node location to goal
      + children --- returns a list of potential node children
      + validation - vets children against open and closed lists with their f and h values, returns updated open list sorted by f values


    plot (Function)
    Plots grid map information

      Parameters:
      + grid -- grid_map that Grid class created
      + path -- path that Astar class creates
      + start - given
      + goal -- given

    main (Function)
    Executes assignment
