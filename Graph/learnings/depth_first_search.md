#Depth First Search
===================

* Recursive algorihm to traverse the graph.
* Use Stack
* Start with root node and traverse deep towards node with no children.
* LIFO principle
* Time complexity = O(V+E) when adjacency list is used
* Time complexity = O(V^2) when adjacency matrix is used
* Childrens are visited before siblings
* Use backtracking


##Advantages:
    * Use less memory
    * At a time it stores only single path from root to leaf. Hence lesser space.
    * Fast
    * When target is far from source, DFS is preffered.


##Disadvantages
    * Not optimal for finding shortest path
    * Takes time to visit neighbouring node if depth is high.


##Application:
    * Maze or sudoko
    * Topological sorting
    * Cycle detection
    * Scheduling problems
