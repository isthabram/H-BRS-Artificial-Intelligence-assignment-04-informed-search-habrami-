from typing import List, Tuple
from utils import print_puzzle

class Puzzle:

    def __init__(self, init_state: List[int], puzzle_type: int = 8):
        """
        Initialize a new 8-puzzle board
        :param init_state: Initial configuration of the board
        """
        self.init_state = init_state
        self.goal_state = [i for i in range(0, 9)]
        # YOUR CODE HERE
        explored=[]

    def goal_test(self, state: List[int]):
        """Test if goal state is reached
        :param state: board configuration to check
        :return: true if the passed configuration is equal to goal configuration
        """
        # YOUR CODE HERE
        if(state == goal_state): 
            return True
        else: 
            return False

    def is_explored(self, state: List[int]):
        """Check if a particular board configuration has already been explored
        :param state: board configuration to check
        :return: true if a particular configuration has already been explored
        """
        # YOUR CODE HERE
        raise NotImplementedError()


def move_left(position: int) -> int:
    """Move one position left in 8 puzzle if possible
    :param position: current position of the 0 tile
    :return: new position of the 0 tile after moving to the left
    """
    # YOUR CODE HERE
    if(position != 0 or position != 3 or position != 6):
        return position-1


def move_right(position: int) -> int:
    """Move one position right in 8 puzzle if possible
    :param position: current position of the 0 tile
    :return: new position of the 0 tile after moving to the right
    """
    # YOUR CODE HERE
    if(position != 2 or position != 5 or position != 8):
        return position+1


def move_up(position: int) -> int:
    """Move one position up in 8 puzzle if possible
    :param position: current position of the 0 tile
    :return: new position of the 0 tile after moving upwards
    """
    # YOUR CODE HERE
    if(position != 0 or position != 1 or position != 2):
        return position-3


def move_down(position: int):
    """Move one position down in 8 puzzle if possible
    :param position: current position of the 0 tile.
    :return: new position of the 0 tile after moving downwards
    """
    # YOUR CODE HERE
    if(position != 6 or position != 7 or position != 8):
        return position+3

    
def up(state: List[int], i) -> List[int]:
    """Determine the new state when the empty tile is moved up
    :param state: current configuration of the puzzle as one dimensional list
               i: the position of the empty tile
    :return: new configuration of the puzzle as one dimensional list
    """
    # Copy the current configuration by value to a temporary list
    tmp = state[:]
        
    # Determine the new position of the empty tile
    nxt_pos = move_up(i)
        
    # Determine the value of the tile which currently on that position
    nxt = state[nxt_pos]
      
    # Swap the empty and the other tile
    tmp[nxt_pos] = 0
    tmp[i] = nxt
    
    return tmp
    
def right(state: List[int], i) -> List[int]:
    """Determine the new state when the empty tile is moved right
    :param state: current configuration of the puzzle as one dimensional list
               i: the position of the empty tile
    :return: new configuration of the puzzle as one dimensional list
    """
    # Copy the current configuration by value to a temporary list
    tmp = state[:]
        
    # Determine the new position of the empty tile
    nxt_pos = move_right(i)
        
    # Determine the value of the tile which currently on that position
    nxt = state[nxt_pos]
      
    # Swap the empty and the other tile
    tmp[nxt_pos] = 0
    tmp[i] = nxt
    
    return tmp

def down(state: List[int], i) -> List[int]:
    """Determine the new state when the empty tile is moved down
    :param state: current configuration of the puzzle as one dimensional list
               i: the position of the empty tile
    :return: new configuration of the puzzle as one dimensional list
    """
    # Copy the current configuration by value to a temporary list
    tmp = state[:]
        
    # Determine the new position of the empty tile
    nxt_pos = move_down(i)
        
    # Determine the value of the tile which currently on that position
    nxt = state[nxt_pos]
      
    # Swap the empty and the other tile
    tmp[nxt_pos] = 0
    tmp[i] = nxt
    
    return tmp

def left(state: List[int], i) -> List[int]:
    """Determine the new state when the empty tile is moved left
    :param state: current configuration of the puzzle as one dimensional list
               i: the position of the empty tile
    :return: new configuration of the puzzle as one dimensional list
    """
    # Copy the current configuration by value to a temporary list
    tmp = state[:]
        
    # Determine the new position of the empty tile
    nxt_pos = move_left(i)
        
    # Determine the value of the tile which currently on that position
    nxt = state[nxt_pos]
      
    # Swap the empty and the other tile
    tmp[nxt_pos] = 0
    tmp[i] = nxt
    
    return tmp
    

def get_possible_moves(state: List[int]) -> List[List[int]]:
    """Check whether a move is possible in left, right, up, down direction and store it.
    :param state: current configuration of the puzzle as one dimensional list
    :return: list containing the new configurations after applying all possible moves
    """
    # YOUR CODE HERE
    possible_moves=[]
    
    # Search the position of the empty tile
    for i, node in enumerate(state):
        if (node == 0): break
            
    '''Check every possibilities '''
    # Position 0 -> move right and down
    if(i == 0):
        tmp = right(state, i)
        possible_moves.append(tmp)
        tmp = down(state, i)
        possible_moves.append(tmp)
    elif(i == 1):
        tmp = right(state, i)
        possible_moves.append(tmp)
        tmp = down(state, i)
        possible_moves.append(tmp)
        tmp = left(state, i)
        possible_moves.append(tmp)
    elif(i == 2):
        tmp = down(state, i)
        possible_moves.append(tmp)
        tmp = left(state, i)
        possible_moves.append(tmp)
    elif(i == 3):
        tmp = up(state, i)
        possible_moves.append(tmp)
        tmp = right(state, i)
        possible_moves.append(tmp)
        tmp = down(state, i)
        possible_moves.append(tmp)
    elif(i == 4):
        tmp = up(state, i)
        possible_moves.append(tmp)
        tmp = right(state, i)
        possible_moves.append(tmp)
        tmp = down(state, i)
        possible_moves.append(tmp)
        tmp = left(state, i)
        possible_moves.append(tmp)
    elif(i == 5):
        tmp = up(state, i)
        possible_moves.append(tmp)
        tmp = left(state, i)
        possible_moves.append(tmp)
        tmp = down(state, i)
        possible_moves.append(tmp)
    elif(i == 6):
        tmp = up(state, i)
        possible_moves.append(tmp)
        tmp = right(state, i)
        possible_moves.append(tmp)
    elif(i == 7):
        tmp = up(state, i)
        possible_moves.append(tmp)
        tmp = right(state, i)
        possible_moves.append(tmp)
        tmp = left(state, i)
        possible_moves.append(tmp)
    elif(i == 8):
        tmp = up(state, i)
        possible_moves.append(tmp)
        tmp = left(state, i)
        possible_moves.append(tmp)
        
    return possible_moves
    