# Data Structures and Algorithms
## Description
This repository contains Python implementations of various data structures and algorithms, as assigned by Grand Valley State University's Data Structures and Algorithms course. As such, these scripts are designed as a learning resource for understanding the principles behind fundamental CS concepts.

## Table of Contents
- B-Trees
- Big O Notation
- Binary Search Trees
- Dynamic Programming - Knapsack Problem
- Hash Tables and Collision Resolution Techniques
- Heaps
- Insertion Sort
- Graphs - Maximum Flow
- Red-Black Trees
- Graphs - Topological Sort

## Installation
To clone and run the scripts locally, use the following command:
`git clone https://github.com/jrkave/Data-Structures-Algorithms.git`

## Usage
Each script in this repository demonstrates a specific data structure or algorithm. You can run them independently to see them in action. Before running any script, ensure Python is installed on your system.

## Scripts Description
### B-Trees
B-trees are self-balancing tree data structures commonly used in database systems to organize and efficiently access large amounts of data. They are designed to provide fast search, insertion, and deletion operations on data that is stored in disk or other secondary storage devices. Each node of a B-tree can have multiple children, and is typically represented with a fixed maximum number of children, known as the order of the B-tree. The order determines the maximum number of keys a node can hold.

B-trees have the following properties:
1. Every node 'x' has the following attributes:
   - n: the number of keys currently stored in node 'x'
   - The 'n' keys themselves: k<sub>1</sub>, k<sub>2</sub>, ... k<sub>n</sub>, stored in nondecreasing order
   - x.leaf, a boolean value that is True is x is a leaf
   - Each internal node contains n keys and n+1 pointers
2. All leaves have the same depth, which is the tree's height, _h_
3. Nodes have lower and upper bounds on the number of keys they contain
   - Lower bound: every node must have at least t-1 keys
   - Upper bound: every node may contain at most 2t-1 keys

View its implementation [here](https://github.com/jrkave/Data-Structures-Algorithms/blob/main/b_trees.py/).

### Big O Notation
This script demonstrates how runtimes differ across functions with differing Big-O notations. Check it out [here](https://github.com/jrkave/Data-Structures-Algorithms/blob/main/big_o_notation.py/).

### Binary Search Trees
A binary search trees (BST) is a rooted binary tree data structure with the key of each internal node being greater than all the keys in the respective node's left subtree and less than the ones in its right subtree. Find the script [here](https://github.com/jrkave/Data-Structures-Algorithms/blob/main/bst.py/). 

### Dynamic Programming - Knapsack Problem
This code demonstrates how to solve the knapsack problem with dynamic programming. It breaks down the knapsack problem into subproblems, stores the results in a matrix, and optimizes the subproblems to find the overall solution. The script can be found [here](https://github.com/jrkave/Data-Structures-Algorithms/blob/main/dp_knapsack.py/).

### Hash Tables and Collision Resolution Techniques
This script implements hashing, or the process of mapping keys and values into a hash table by using a hash function, using the following four collision resolution techniques:
1. Linear probing: when two or more keys hash to the same index, the algorithm tries to place the value in the next available spot in the array
2. Quadratic probing: instead of looking at the next spot (as with linear probing), this algorithm jumps ahead by incrementing the original hash index by the square of the index, avoiding clusters that occur in linear probing
3. Double hashing: this technique uses a secondary hash function when a collision occurs, with the idea being that if the first hash function causes a collision, the second hash function likely won't 
4. Chaining: this method creates a list at each index of the hash table, and all elements that hash to a certain index are stored in the list at that index

View the script [here](https://github.com/jrkave/Data-Structures-Algorithms/blob/main/hash_tables.py/).

### Heaps
This script implements a Max Heap, or a complete binary tree in which the value of a node is greater than or equal to the value of its children. Heaps are particularly useful when one wants to quickly retrieve the maximum or minimum elements very quickly. See it implemented [here](https://github.com/jrkave/Data-Structures-Algorithms/blob/main/heaps.py/).

### Insertion Sort
This simple script demonstrates insertion sort. You can find [here](https://github.com/jrkave/Data-Structures-Algorithms/blob/main/insertion_sort.py/). 

### Graphs - Maximum Flow
This script uses the Ford Fulkerson algorithm to find the maximum flow of a directed acyclic graph (DAG). Check it out [here](https://github.com/jrkave/Data-Structures-Algorithms/blob/main/maximum_flow.py/).

### Red-Black Trees
This script implements are red-black tree, a specialized self-balancing tree data structure in which every node is either red or black. 

Red-black trees have the following properites:
1. It is a self-balancing binary search tree
2. Every node is either red or black
3. The root is always black
4. Every leaf, which is nil, is black
5. If a node is red, then its children are black
6. Every path from a node to any of its descendant nil node has the same number of black nodes (including the nil node)

During insertion, updation, and deletion operations, the red-black tree may undergo rotation and/or recoloring operations to preserve the balancing properties of the tree.

See it implemented [here](https://github.com/jrkave/Data-Structures-Algorithms/blob/main/rb_trees.py/).

### Graphs - Topological Sort
This script implements topological sort, defined as a linear ordering of vertices of a directed acyclic graph (DAG) such that for every directed edge _u_ -> _v_, vertex _u_ comes before _v_ in the ordering. Check it out [here](https://github.com/jrkave/Data-Structures-Algorithms/blob/main/top_sort.py/).


