from import_library import *

class BFS:
    def __init__(self, graph):
        self.graph = graph
        self.visited = []
        self.queue  = []
        self.bfs = []
    
    def do_bfs(self, start_node_idx):
        key = start_node_idx
        self.queue.append(key)
        self.visited.append(key)

        while self.queue:
            current_node_idx = self.queue.pop(0)
            self.bfs.append(self.graph[current_node_idx].name)
        
            for child in self.graph[current_node_idx].children:
                child_idx = child.id
                if child_idx not in self.visited:
                    self.visited.append(child_idx)
                    self.queue.append(child_idx)


