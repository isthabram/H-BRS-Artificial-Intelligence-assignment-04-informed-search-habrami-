def hamming_distance(state: List[int]) -> int:
    """Calculate the Hamming distance for a particular configuration
    :param state: current configuration of the puzzle
    :return: the number of misplaced tiles in the given configuration
    """
    # YOUR CODE HERE
    dist=0
    for i, tile in enumerate(state):
        if(tile != i):
            dist += 1
    
    return dist

def manhattan_helper(num: int, x_: int, y_: int) -> int:
    goal = [[0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]]
    
    dist = 0
    
    for x, row in enumerate(goal):
        for y, tile in enumerate(row):
            if(num == goal[x][y]):
                dist = abs(x-x_) + abs(y-y_)
                break
    
    return dist
    

def manhattan_distance(state: List[int]) -> int:
    """Function to calculate the manhattan distance for a
    particular configuration
    :param state: current configuration of the puzzle
    :return: the accumulated manhattan distance between each tile and its goal position in the given configuration
    """
    # YOUR CODE HERE
    dist = 0
    
    DD = [[state[0], state[1], state[2]],
          [state[3], state[4], state[5]],
          [state[6], state[7], state[8]]]
    
    goal = [[0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]]
    
    for x, row in enumerate(DD):
        for y, tile in enumerate(row):
            if(DD[x][y] != goal[x][y]):
                dist += manhattan_helper(DD[x][y], x, y)

    return dist