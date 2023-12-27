import copy

class TreeNode:
    def __init__(self,value,move=(0,0)):
        self.value=value
        self.children=[]
        self.parent=None
        self.move=move
    
    def add_child(self,child):
        child.parent=self
        self.children.append(child)

def generate_next_state(current_state, action):
    next_state = copy.deepcopy(current_state)
    empty_row, empty_col = find_empty_tile(next_state)
    move_row, move_col = action
    next_row, next_col = empty_row + move_row, empty_col + move_col

    if 0 <= next_row < len(current_state) and 0 <= next_col < len(current_state[0]):
        next_state[empty_row][empty_col] = next_state[next_row][next_col]
        next_state[next_row][next_col] = 0
        return next_state
    else:
        return None  

def find_empty_tile(state):
    for row in range(len(state)):
        for col in range(len(state[row])):
            if state[row][col] == 0:
                return row, col

def is_goal_state(state, goal_state):
    return state == goal_state

def print_puzzle(state):
    for row in state:
        print(' '.join(map(str, row)))
    print()



def breadth_first_search(initial_state, target_state):
    visited_states = []
    visited_states.append([initial_state, []])
    queue = []
    queue.append([initial_state, []])
    (current_state, move) = queue.pop(0)

    while current_state != target_state:
        possible_moves = [[0,-1], [0,1], [-1,0], [1,0]]
        for i in range(len(possible_moves)):
            next_state = generate_next_state(current_state, possible_moves[i])
            if next_state is not None:
                if next_state not in visited_states:
                    queue.append([next_state, possible_moves[i]])
                    visited_states.append([next_state, possible_moves[i]])
        current_state, move = queue.pop(0)

    solution_path = []
    solution_path.append(current_state)
    backtrack_state = current_state
    backtrack_move = move

    while backtrack_state != initial_state:
        for i in range(2):
            backtrack_move[i] = -backtrack_move[i]
        previous_state = generate_next_state(backtrack_state, backtrack_move)
        for k in visited_states:
            if k[0] == previous_state:
                backtrack_move = k[1]
                solution_path.insert(0, (previous_state, k[1]))
                backtrack_state = previous_state
                break

    return solution_path

possible_moves = [[0,-1], [0,1], [-1,0], [1,0]]
def depth_first_search(initial_state, target_state):
    visited_states = []
    node_stack = [TreeNode(initial_state)]
    goal_node = None

    while node_stack:
        current_node = node_stack.pop()
        if current_node.value == target_state:
            visited_states.append(current_node.value)
            goal_node = current_node
            break

        if current_node.value not in visited_states:
            visited_states.append(current_node.value)
            for move in possible_moves:
                next_state = generate_next_state(current_node.value, move)
                if next_state is not None:
                    child_node = TreeNode(next_state)
                    child_node.move = move
                    current_node.add_child(child_node)
                    node_stack.append(child_node)

    if not node_stack:
        return None

    if goal_node:
        solution_path = [(goal_node.value, 'Solution found')]
        while goal_node.parent is not None:
            solution_path.append((goal_node.parent.value, goal_node.move))
            goal_node = goal_node.parent

    solution_path.reverse()
    return solution_path


start_state = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

print("Depth-First Search:")
solution_dfs = depth_first_search(start_state, goal_state)
if solution_dfs:
    for step in solution_dfs:
        state, action = step
        print_puzzle(state)
        print("Action:", action)
        print(f'No. of steps in dfs- {len(solution_dfs)-1}')
else:
    print("No solution found.")

print("Breadth-First Search:")
solution_bfs = breadth_first_search(start_state, goal_state)
if solution_bfs:
    for step in solution_bfs:
        state= step
        print_puzzle(state)
        print(f'No. of steps in bfs-{len(solution_bfs)-1}')
else:
    print("No solution found.")
