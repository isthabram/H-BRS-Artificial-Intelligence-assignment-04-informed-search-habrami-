import matplotlib.pyplot as plt
from numpy.core.fromnumeric import sort
from evaluation_a import *

import random

def inversion(configuration: List[int]) -> int:
    """
    Finds all inversions in a puzzle configuration and returns their total number
    :param configuration: the configuration of the 8 puzzle to count its inversions
    :returns: number of inversions in the puzzle configuration
    """
    inv = 0
    for i, elem in enumerate(configuration):
        for j, sg in enumerate(configuration):
            if(j > i and configuration[i] > configuration[j] and elem != 0 and sg != 0):
                inv += 1

    return inv

def is_solvable(configuration: List[int]) -> bool:
    """
    Checks whether a given puzzle configuration is solvable or not
    :param configuration: the initial configuration of the puzzle to check for solvability
    :returns: True if the configuration is solvable; False otherwise
    """
    inv = inversion(configuration)

    row = 0
    for i, elem in enumerate(configuration):
        if elem == 0:
            row = i
            break
    
    row = (row // 3) 
    
    if (inv+row)%2 == 0:
        return True
    else:
        return False

hundred=[]
one=[0, 1, 2, 3, 4, 5, 6, 7, 8]
complexity=[]

# Generate 100 solvable configuration
while len(hundred) < 100:
    random.shuffle(one)
    if one not in hundred and is_solvable(one):
        hundred.append(list(one))

# Calculate the complexity for each configuration
for i, elem in enumerate(hundred):
    complexity.append(inversion(elem))

# Sort the configuration based on the complexity
hundred = [x for _, x in sorted(zip(complexity, hundred))]
complexity.sort()

time_s_m=[]
cost_s_m=[]
node_s_m=[]

for i in hundred:
    start = time.time()
    a, b  = astar_search(Puzzle(i), manhattan_distance)
    end = time.time()
    cost_s_m.append(len(a))
    node_s_m.append(b)
    time_s_m.append(end-start)

time_s_h=[]
cost_s_h=[]
node_s_h=[]

for i in hundred:
    start = time.time()
    a, b  = astar_search(Puzzle(i), hamming_distance)
    end = time.time()
    cost_s_h.append(len(a))
    node_s_h.append(b)
    time_s_h.append(end-start)

time_g_m=[]
cost_g_m=[]
node_g_m=[]

for i in hundred:
    start = time.time()
    a, b  = greedy_search(Puzzle(i), manhattan_distance)
    end = time.time()
    cost_g_m.append(len(a))
    node_g_m.append(b)
    time_g_m.append(end-start)

time_g_h=[]
cost_g_h=[]
node_g_h=[]

for i in hundred:
    start = time.time()
    a, b  = greedy_search(Puzzle(i), hamming_distance)
    end = time.time()
    cost_g_h.append(len(a))
    node_g_h.append(b)
    time_g_h.append(end-start)

fig, (ax1, ax2, ax3) = plt.subplots(3)
ax1.plot(complexity, time_s_m, label='A*, manhattan')
ax2.plot(complexity, cost_s_m, label='A*, manhattan')
ax3.plot(complexity, node_s_m, label='A*, manhattan')
ax1.plot(complexity, time_s_h, c='r', label='A*, hamming')
ax2.plot(complexity, cost_s_h, c='r', label='A*, hamming')
ax3.plot(complexity, node_s_h, c='r', label='A*, hamming')
ax1.plot(complexity, time_g_m, c='g', label='Greedy, manhattan')
ax2.plot(complexity, cost_g_m, c='g', label='Greedy, manhattan')
ax3.plot(complexity, node_g_m, c='g', label='Greedy, manhattan')
ax1.plot(complexity, time_g_h, 'tab:pink', label='Greedy, hamming')
ax2.plot(complexity, cost_g_h, 'tab:pink', label='Greedy, hamming')
ax3.plot(complexity, node_g_h, 'tab:pink', label='Greedy, hamming')

ax1.set(ylabel='time [s]')
ax2.set(ylabel='depth')
ax3.set(ylabel='explored nodes')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=5)
plt.show()