from import_library import *

class DFS:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        self.dfs = []

    def do_dfs(self, node_idx):  #function for dfs 
        key = node_idx
        node = self.graph[key]
        if key not in self.visited:
            self.dfs.append(self.graph[key].name)
            self.visited.add(key)
            for child in self.graph[key].children:
                self.do_dfs(child.id)
