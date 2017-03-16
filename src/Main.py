# initializing initial and goal state
initial_state = 7
goal_state = 0

# initializing transition matrix
TM = []
TM.append([0,2,0,1])
TM.append([1,5,0,1])
TM.append([2,2,2,3])
TM.append([3,7,2,3])
TM.append([4,6,4,5])
TM.append([5,5,4,5])
TM.append([6,6,6,7])
TM.append([7,7,6,7])

# initialize the frontier using the initial state of problem
frontier = [initial_state,]

# initialize the explored set to be empty
explored_set = []

# loop do
while True:
    
    # if the frontier is empty then return failure
    if not frontier:
        print("goal not found")
        break
    else:
        # choose a leaf node and remove it from the frontier
        state = frontier[0]
        frontier.remove(state)
        # if the node contains a goal state then return the corresponding solution
        if state == goal_state:
            print("goal found")
            break
        else:
            # add the node to the explored set
            explored_set.append(state)
            # expand the chosen node, adding the resulting nodes to the frontier
            # only if not in the frontier or explored set
            for child in TM[state]:
                if child in explored_set or child in frontier:
                    pass
                else:
                    frontier.append(child)