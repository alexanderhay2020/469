# ME 469 - Homework 1B

Alexander Hay<br/>
ME 469, HW1, Part B<br/>
A* Search and Navigation

## Preface

Run 'run.py' via python.

Press 'q' to step through figures

---------------------------------
## Code Breakdown

### Imports and Global Variables:

##### Imports:
+ numpy
+ matplotlib
+ math

##### Global Variables:
+ barcodes -> ds1_Barcodes.dat
+ groundtruth -> ds1_Groundtruth.dat
+ landmark -> ds1_Landmark_Groundtruth.dat
+ measurement -> ds1_Measurement.dat
+ odometry -> ds1_Odometry.dat

### Classes and Functions

#### Node (Class)
&nbsp;&nbsp;Defines attributes for each node<br/>

##### Parameters:
+ parent &nbsp;&nbsp;&nbsp; tuple (x,y) of parent node, starting node has no parent
+ position &nbsp; tuple (x,y) of itself

##### Attributes:
+ parent &nbsp;&nbsp;&nbsp;&nbsp; parent node
+ position &nbsp; (x,y)
+ g &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; distance from node to start
+ h &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; distance from node to goal (heuristic)
+ f &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; g + h (cost function)


#### Grid (Class)
&nbsp;&nbsp;Sets grid_map node size and node cost
##### Parameters:
+ node size &nbsp;&nbsp;&nbsp; float of the size of the node in meters
+ start &nbsp;&nbsp;&nbsp; tuple (x,y) of start node
+ goal &nbsp;&nbsp;&nbsp; tuple (x,y) of goal node

##### Attributes:
+ start &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; starting node in grid coordinates
+ goal &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; goal node in grid coordinates
+ landmark_list &nbsp;&nbsp; list of landmarks (used for debugging)
+ xedges &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; an array of the x coordinates for nodes the grid_map is built of
+ yedges &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; an array of the y coordinates for nodes the grid_map is built of
+ node_cost &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; the cost of entering that node

##### Functions:
+ set_cell &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; determines how many nodes to populate world with and their size
+ landmarks &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; converts landmark point to a node, sets node_cost of landmark node to 1000
+ world_to_grid &nbsp;&nbsp; converts world points to their nodes points


#### Astar (Class)
&nbsp;&nbsp; A* algorithm

##### Parameters:
+ start &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; raw start location
+ goal &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; raw goal location
+ grid_map &nbsp;&nbsp;&nbsp; map created by Grid class

##### Attributes:
+ start &nbsp;&nbsp;&nbsp;&nbsp; start location relative to the grip map
+ goal &nbsp;&nbsp;&nbsp;&nbsp; goal location relative to the grip

##### Functions:
+ heuristic &nbsp;&nbsp;&nbsp;&nbsp; calculates the minimum cost from node location to goal
+ children &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; returns a list of potential node children
+ validation &nbsp;&nbsp; vets children against open and closed lists with their f and h values, returns updated open list sorted by f values


#### plot (Function)
&nbsp;&nbsp; Plots grid map information
##### Parameters:
+ grid &nbsp;&nbsp;&nbsp; grid_map that Grid class created
+ path &nbsp;&nbsp; path that Astar class creates
+ start &nbsp;&nbsp; given
+ goal &nbsp;&nbsp; given

#### main (Function)
Executes assignment

<!-- **bold** -->
