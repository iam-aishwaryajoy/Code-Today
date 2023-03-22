BREADTH FIRST SEARCH:
=====================

* Used to traverse a graph or tree. Traversing means visiting each node of the graph.
* Recursive algorithm, but not a backtracking algorithm
* BFS uses Queue to find shortest path.
* All nodes in the same level is visited first
* FIFO principle
* Time complexity = O(V+E), when adjacency list is used
* Time complexity = O(V^2) when adjacency matrix is used
* Siblings are visited before children

# Advantages:
* When target is close to source BFS is preffered than DFS.

# Disadvantage:
* Slow because space complexity is high
* More memory

# Application:
* Cycle detection in unididrected graph
* Shortest path
* In GPS, to find nieghbouring place.
* In networking, to broadcast packets.

