# Solving 8-Puzzle Problem using BFS and DFS

This repository contains a Python implementation that solves the classic 8-puzzle problem using two distinct graph traversal algorithm strategies: **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**.

## Overview
The 8-puzzle problem involves moving tiles in a 3x3 grid to arrive at a target state. This implementation tracks the path from a start state to a goal state. 

### Implementation Highlights
- **`142201015.py`**: The core script defining the application logic:
  - `TreeNode` for graphing states.
  - State generator logic (`generate_next_state`) mapping empty tile (`0`) permutations natively to valid movement dimensions (Left, Right, Up, Down).
  - Explicit function blocks handling DFS (using tree nodes) and BFS (using queued array iterations).
  
### Running the Code
```bash
python3 142201015.py
```
Outputs the sequential puzzle grids forming the solution paths for both BFS and DFS methodologies alongside step statistics.
