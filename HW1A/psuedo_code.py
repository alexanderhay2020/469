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



A* Algorithm:

    Initialize grid

1   Initialize node costs (1)
        for i in range(len(xedges)):
            for j in range(len(yedges)):
                grid_map[i,j].g = 1
            /loop
        /loop

    Initialize barrier costs (1000)
        for i in range(len(landmarks)):
            grid_map[[landmark[i],1],[landmark[i],2]].g = 1000

    Identify start/goal nodes

    node = grid_map(start_coords)
    goal = grid_map(goal_coords)

    Initialize costs
4       node.g = distance from node to start
            node.g = 1
        node.h = distance from node to goal; heuristic
        node.f = g + h cost function; estimate of best route to node (we want the lowest cost)

    Initiate open list []

    Initiate closed list []
        - Add start node to open list

    *loop while open list is not empty
    while len(open_list) > 0:
        a) find node with least f on open list,
           call it node q

        b) pop q off open list
           put q on closed list

        c) generate q's 8 successors
            child_list = [
            [qx-1,qy+1],[qx,qy+1],[qx+1,qy+1]
               [qx-1,0],[qx, qy] ,[qx+1,0]
            [qx-1,qy-1],[qx,qy-1],[qx+1,qy-1]
            ]

            *calculate child's parameters
            for i in range(len(child_list)):
                child_list[i].parent = q
2               child_list[i].g = child_list[i].parent.g + node.g
            /loop

            *check if any children is the goal
            *putting this here means that the algorithm doesn't care if the goal is a landmark
            for i in range(len(child_list)):
                if child_list[i] == goal:
3                   return child_list[i].parent

            *checks if child is parent
            for i in range(len(child_list)):
                if child_list[i] == child_list[i].parent:
                    remove child_list[i] from child_list

            *check if child is out of bounds
            for i in range(len(child_list)):
                if child_list[i].x < -2 or child_list[i].x > 4 or
                   child_list[i].y < -6 or child_list[i].y > 5:
                   remove child_list[i] from child_list
                endif
            /loop

2           *check if child is a landmark
            for i in range(len(child_list)):
                for j in range(len(landmark)):
                    if child_list[i] == landmark[j]:
                        remove child_list[i] from child_list
                    endif
                /loop
            /loop

            * check if child is on closed/open list, and if so, checks for lower f cost
            for i in range(len(child_list)):
                for j in range(len(closed_list)):
                    if child_list[i] == closed_list[j]:
                        if child_list[i].f > closed_list[j].f:
                            remove child_list[i] from child_list
                        endif
                    endif
                /loop
                for k in range(len(open_list)):
                    if child_list[i] == open_list[j]:
                        if child_list[i].f > open_list[j].f:
                            remove child_list[i] from child_list
                        endif
                    endif
            /loop

            * add child with lowest f to open list
            * if tie, add child with lowest h to open list
            Don't even know what this code would look like, never sorted in python before

    plot point for each node in closed list

    plot path from goal (from point to point)
    """
