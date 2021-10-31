from heuristic import *
from puzzle import *
from typing import Callable, Tuple, List

class Node:

    def __init__(self, state: List[int], parent: int, g: int, h: int):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g+h

def isIn(lista: List[Node], elem: List[int]) -> bool:
    '''
    Returns true, if the elem is in the list
    Returns false, if the elem is in NOT the list
    '''
    for i in lista:
        if(i.state == elem): 
            return True

    return False

def astar_search(board: Puzzle, heuristic: Callable) -> Tuple[List[int], int]:
    """
    :param board: the 8-puzzle to solve
    :param heuristic: the heuristic function to use
    :return: an ordered list with the solution path and the number of total nodes expanded
    """
    # YOUR CODE HERE
    closed=[]
    fringe=[]
    fringe.append(Node(board.init_state, None, 0, heuristic(board.init_state)))
    while len(fringe) > 0:

        # Find node with the least f value in fringe
        node = fringe[0]
        i = 0
        for j, tmp in enumerate(fringe):
            if tmp.f < node.f:
                node = fringe[j]
                i = j-1

        # Pop this node from fringe and append to closed
        fringe.pop(i)
        closed.append(node)

        # Check if this node is at the goal state or not
        if(board.goal_test(node.state)):
            break

        # Generate the successors of this node 
        # Append them to the fringe, if this node is not already explored
        children = get_possible_moves(closed[-1].state)
        for tmp in children:
            if(isIn(closed, tmp) == False and isIn(fringe, tmp) == False):
                fringe.append(Node(tmp, len(closed)-1, closed[-1].g + 2, heuristic(tmp)))       

    solution=[]
    node = closed[-1]
    solution.append(node.state)
    while node.parent != None:
        node = closed[node.parent]
        solution.append(node.state)

    length = len(closed) + len(fringe)
    
    return solution, length
            

p = Puzzle([0,1,2,3,4,5,8,6,7])
path, expanded_nodes = astar_search(p, manhattan_distance)

'''for i in path:
    print(i)

print("Path length: ", len(path))
print("Expanded nodes: ", expanded_nodes)'''