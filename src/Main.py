initial_state = 7
goal_state = 0

TM = []
TM.append([0,2,0,1])
TM.append([1,5,0,1])
TM.append([2,2,2,3])
TM.append([3,7,2,3])
TM.append([4,6,4,5])
TM.append([5,5,4,5])
TM.append([6,6,6,7])
TM.append([7,7,6,7])

frontier = [initial_state,]
explored_set = []

while True:
    if not frontier:
        print("goal not found")
        break
    else:
        state = frontier[0]
        frontier.remove(state)
        if state == goal_state:
            print("goal found")
            break
        else:
            explored_set.append(state)
            for child in TM[state]:
                if child in explored_set or child in frontier:
                    pass
                else:
                    frontier.append(child)