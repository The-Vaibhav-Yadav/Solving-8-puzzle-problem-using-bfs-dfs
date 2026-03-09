# 8-Puzzle Problem Solver

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

An algorithmic solver for the classic sliding 8-puzzle game. This project maps matrix permutations into mathematically contiguous state tree structures and compares Breadth-First Search (BFS) against Depth-First Search (DFS) for pathfinding optimality and time complexity metrics.

## Table of Contents
- [Tech Stack & Architecture](#tech-stack--architecture)
- [Prerequisites](#prerequisites)
- [Installation & Local Setup](#installation--local-setup)
- [Usage & Running the App](#usage--running-the-app)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing Guidelines](#contributing-guidelines)
- [License and Contact](#license-and-contact)

## Tech Stack & Architecture

- **Language**: Python (Standard Library only)
- **Concepts**: Graph Traversal, State Trees, Matrix Manipulation.

**High-Level Architecture**: 
- `TreeNode`: A Python class that encapsulates a grid matrix along with its parental backlink and the transitional directional movement (action).
- `generate_next_state(state, action)`: Core engine that maps the `0` (empty tile), calculates offset boundary limits, and yields the mutated adjacent state.
- `breadth_first_search()` & `depth_first_search()`: Traversal functions utilizing list-based Queues and Stacks to explore the entire configuration space until `goal_state` matched.

## Prerequisites
- **Python**: Version 3.8+ or higher.

## Installation & Local Setup

```bash
git clone https://github.com/The-Vaibhav-Yadav/Solving-8-puzzle-problem-using-bfs-dfs.git
cd Solving-8-puzzle-problem-using-bfs-dfs
```

There are no external dependencies, `pip` installations, or environment variables required (.env).

## Usage & Running the App
Run the solver script directly via the shell to resolve the built-in starting puzzle matrix.

```bash
python3 142201015.py
```
**Expected Output**:
The terminal prints the sequential 3x3 matrices demonstrating the steps taken to reach the goal grid, followed by quantitative text detailing the total step operations executed by DFS vs BFS.

## Testing
This project acts as an algorithmic academic script. To verify functionality, validate the output state grids computationally or visually against expected shortest-path transitions. Further tests can be written using `pytest`.

```bash
# Example pytest format
pytest tests/
```

## Deployment
As this is a pure computational script, remote deployment isn't typically necessary. Simply clone the repository or embed the logic in larger gaming/system backends as a Python import module.

## Contributing Guidelines
1. Fork the repository
2. Create your Feature Branch (`git checkout -b feature/Optimization`)
3. Commit your Changes using Conventional Commits (`git commit -m 'feat: optimized BFS visited state lookups using sets instead of lists'`)
4. Push to the Branch (`git push origin feature/Optimization`)
5. Open a Pull Request

**Code Style**: Stick to rigid PEP-8 formatting guidelines.

## License and Contact
- **License**: MIT
- **Contact**: Vaibhav Yadav (https://github.com/The-Vaibhav-Yadav)
