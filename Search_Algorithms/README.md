# CS50 AI: Chapter 0 - Search

Welcome to the repository for Chapter 0 of the CS50 AI course by Harvard University! This chapter provides an introduction to search algorithms, which are fundamental in the field of artificial intelligence. These algorithms help in exploring and navigating through complex problem spaces to find solutions.

## Table of Contents

- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
- [Search Algorithms](#search-algorithms)
  - [Uninformed Search](#uninformed-search)
  - [Informed Search](#informed-search)
- [Implementation Examples](#implementation-examples)
- [Resources and Further Reading](#resources-and-further-reading)
- [Acknowledgments](#acknowledgments)
- [License](#license)

## Introduction

In artificial intelligence, search algorithms are used to explore possible actions and states to solve problems. Whether it's finding the shortest path in a maze or solving a puzzle, search algorithms are crucial for navigating complex problem spaces.

Chapter 0 of CS50 AI covers the foundational concepts and types of search algorithms that are key to AI applications. This chapter will introduce both uninformed and informed search strategies and demonstrate their practical applications.

## Key Concepts

- **State Space**: Represents all possible states or configurations within a problem domain.
- **Search Space**: Comprises all possible actions or steps that transition from one state to another.
- **Search Tree**: A hierarchical structure where nodes represent states and edges represent actions leading to new states.

## Search Algorithms

### Uninformed Search

Uninformed search algorithms explore the search space without additional information about which direction might lead to a solution. They include:

- **Breadth-First Search (BFS)**: 
  - **Description**: Explores all nodes at the current depth level before moving on to nodes at the next level.
  - **Advantages**: Guarantees finding the shortest path in an unweighted graph.
  - **Use Cases**: Suitable for problems where the shortest path needs to be found.

- **Depth-First Search (DFS)**: 
  - **Description**: Explores as far as possible along each branch before backtracking.
  - **Advantages**: Can be more memory efficient compared to BFS.
  - **Use Cases**: Useful in scenarios where memory is limited, and finding the shortest path is not critical.

### Informed Search

Informed search algorithms use heuristic information to guide the search more efficiently. They include:

- **A* Search**: 
  - **Description**: Combines the cost to reach a node and an estimate of the cost to reach the goal (heuristic) to find the shortest path.
  - **Advantages**: Finds the optimal path by considering both actual and estimated costs.
  - **Use Cases**: Ideal for pathfinding problems where heuristic information is available.

- **Greedy Search**: 
  - **Description**: Uses only the heuristic to guide the search.
  - **Advantages**: Aims to reach the goal quickly but does not guarantee the shortest path.
  - **Use Cases**: Effective in scenarios where heuristic information provides good guidance.

## Implementation Examples

This repository includes Python implementations of various search algorithms:

- **`bfs.py`**: Implementation of Breadth-First Search, useful for solving puzzles and pathfinding problems.
- **`dfs.py`**: Implementation of Depth-First Search, demonstrating tree traversal techniques.
- **`a_star.py`**: Implementation of A* Search, showing its application in pathfinding problems.
- **`greedy_search.py`**: Implementation of Greedy Search, useful when heuristic guidance is available.

## Resources and Further Reading

To further explore search algorithms and their applications, consider the following resources:

- [CS50 AI Course Material](https://cs50.harvard.edu/ai/)
- **Artificial Intelligence: A Modern Approach** by Stuart Russell and Peter Norvig
- [Introduction to Algorithms](https://mitpress.mit.edu/9780262033848/introduction-to-algorithms/) by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein

## Acknowledgments

A special thanks to the CS50 team and course instructors for providing a comprehensive introduction to search algorithms. Additional thanks to the online community for their support and resources.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to explore the code and provide feedback. Happy learning!

