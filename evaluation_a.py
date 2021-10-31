from puzzle import *
from heuristic import *
from astar_search import *
from greedy_search import *
import time

def eval_helper(puzzle: int, algorithm: Callable, heuristic: Callable):

    configurations=[[0, 1, 2, 3, 4, 5, 8, 6, 7],
                    [8, 7, 6, 5, 1, 4, 2, 0, 3],
                    [1, 5, 7, 3, 6, 2, 0, 4, 8]]
    
    start = time.time()
    path, expanded_nodes = algorithm(Puzzle(configurations[puzzle-1]), heuristic)
    end = time.time()

    d = {
        'puzzle': puzzle,
        'algorithm': algorithm.__name__,
        'heuristic': heuristic.__name__,
        'expanded nodes': expanded_nodes,
        'execution time': end-start,
        'path cost': len(path)
    }
    return d

evaluation_results = []
evaluation_results.append(eval_helper(1, astar_search, manhattan_distance))
evaluation_results.append(eval_helper(2, astar_search, manhattan_distance))
evaluation_results.append(eval_helper(3, astar_search, manhattan_distance))
evaluation_results.append(eval_helper(1, astar_search, hamming_distance))
evaluation_results.append(eval_helper(2, astar_search, hamming_distance))
evaluation_results.append(eval_helper(3, astar_search, hamming_distance))
evaluation_results.append(eval_helper(1, greedy_search, manhattan_distance))
evaluation_results.append(eval_helper(2, greedy_search, manhattan_distance))
evaluation_results.append(eval_helper(3, greedy_search, manhattan_distance))
evaluation_results.append(eval_helper(1, greedy_search, hamming_distance))
evaluation_results.append(eval_helper(2, greedy_search, hamming_distance))
evaluation_results.append(eval_helper(3, greedy_search, hamming_distance))

print(evaluation_results)
