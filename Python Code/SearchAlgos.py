import random

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For Search Algorithms 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
queue = []
informedQueue = []

'''
BFS add to queue 
regular queue
'''
def add_to_queue_BFS(node_id, parent_node_id, cost, initialize=False):
    #opperates like a regular queue
    if initialize == True:
        del queue[:]
    tup = (node_id, parent_node_id)
    queue.append(tup)
    return queue

'''
BFS add to queue 
'''
def is_queue_empty_BFS():
    if len(queue)>0:
        return False
    return True

'''
BFS pop from queue
'''
def pop_front_BFS():
    (node_id, parent_node_id) = (0, 0)
    return queue.pop(0)

'''
DFS add to queue 
'''
def add_to_queue_DFS(node_id, parent_node_id, cost, initialize=False):
    #opperates like a stack so add to top of stack (bottom of list)
    if initialize == True:
        del queue[:]
    tup = (node_id, parent_node_id)
    queue.append(tup)
    return queue

'''
DFS add to queue 
'''
def is_queue_empty_DFS():
    if len(queue)>0:
        return False
    return True

'''
DFS pop from queue
'''
def pop_front_DFS():
    return queue.pop()

'''
UC add to queue 
'''
def add_to_queue_UC(node_id, parent_node_id, cost, initialize=False):
    iQueue = []
    if initialize == True:
        del informedQueue[:]
        informedQueue.append([node_id, parent_node_id, cost])
    else:
        informedQueue.append([node_id, parent_node_id, cost])
        informedQueue.sort(key=lambda x: x[2])
    for i in informedQueue:
        tup = (i[0], i[1])
        iQueue.append(tup)
    return iQueue

'''
UC add to queue 
'''
def is_queue_empty_UC():
    if len(informedQueue)>0:
        return False
    return True

'''
UC pop from queue
'''
def pop_front_UC():

    (node_id, parent_node_id) = (informedQueue[0][0], informedQueue[0][1])
    informedQueue.pop(0)
    return (node_id, parent_node_id)

'''
A* add to queue 
'''
def add_to_queue_ASTAR(node_id, parent_node_id, cost, initialize=False):
    iQueue = []
    if initialize == True:
        del informedQueue[:]
        informedQueue.append([node_id, parent_node_id, cost])
    else:
        informedQueue.append([node_id, parent_node_id, cost])
        informedQueue.sort(key= lambda x: x[2])

    for i in informedQueue:
        tup = (i[0], i[1])
        iQueue.append(tup)
    return iQueue

'''
A* add to queue 
'''
def is_queue_empty_ASTAR():
    # Your code here
    if len(informedQueue)>0:
        return False
    return True

'''
A* pop from queue
'''
def pop_front_ASTAR():
    (node_id, parent_node_id) = (informedQueue[0][0], informedQueue[0][1])
    informedQueue.pop(0)
    return (node_id, parent_node_id)

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For n-queens problem 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''


'''
Compute a random state 
'''
def get_random_state(n):
    i = 0
    state = []
    while i < n:
        randrow = random.randint(0, n-1)
        state.append(randrow)
        i+=1
    return state

'''
Compute pairs of queens in conflict 
'''
def compute_attacking_pairs(state):
    number_attacking_pairs = 0
    x = 0
    while x < len(state):
        y = x + 1
        while y < len(state):
            if state[x] == state[y] or abs(state[x] - state[y]) == y - x:
                number_attacking_pairs += 1
            y+=1
        x+=1

    return number_attacking_pairs

'''
The basic hill-climing algorithm for n queens
'''
def hill_desending_n_queens(state, comp_att_pairs):
    currentCost = comp_att_pairs(state)
    col = 0
    while col < len(state):
        row = 0
        while row < len(state):
            if row == state[col]:
                row+=1
                continue
            statecopy = state[:]
            statecopy[col] = row
            cost = comp_att_pairs(statecopy)
            if (currentCost > cost):
                state[col] = row
                currentCost = cost
                break
            row+=1
        col+=1
    return state

'''
Hill-climing algorithm for n queens with restart
'''
def n_queens(n, get_rand_st, comp_att_pairs, hill_descending):
    while True:
        random_position = get_rand_st(n)
        possible_solution = hill_descending(random_position, comp_att_pairs)
        if comp_att_pairs(possible_solution) == 0:
            return possible_solution
        else:
            continue