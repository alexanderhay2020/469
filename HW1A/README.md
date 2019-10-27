# ME 469 - Homework 1B

Alexander Hay<br/>
ME 469, HW1, Part B

---------------------------------
## Code Breakdown

### Imports and Global Variables:

##### Imports:
+ numpy
+ matplotlib
+ math

##### Global Variables
+ barcodes -> ds1_Barcodes.dat
+ groundtruth -> ds1_Groundtruth.dat
+ landmark -> ds1_Landmark_Groundtruth.dat
+ measurement -> ds1_Measurement.dat
+ odometry -> ds1_Odometry.dat

### Classes and Functions

#### Node (Class)
Defines attributes for each node<br/>
Attributes:
+ parent &nbsp;&nbsp;&nbsp; parent node
+ position &nbsp; (x,y)
+ g &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; distance from node to start
+ h &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; distance from node to goal (heuristic)
+ f &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; g + h (cost function)

##### Grid (Class)
Sets grid_map node size and node cost
Attributes:
+ start &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; starting node in grid coordinates
+ goal &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; goal node in grid coordinates
+ landmark_list &nbsp;&nbsp; list of landmarks (used for debugging)
+ xedges &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; an array of the x coordinates for nodes the grid_map is built of
+ yedges &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; an array of the y coordinates for nodes the grid_map is built of
+ node_cost &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; the cost of entering that node

    Functions:
    set_cell ------ determines how many nodes to populate world with and their size
    landmarks ----- converts landmark point to a node, sets node_cost of landmark node to 1000
    world_to_grid - converts world points to their nodes points



<!-- **bold** -->
