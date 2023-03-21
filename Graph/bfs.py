class BFS:
    def __init__(self, graph):
        self.graph = graph
        self.visited = []
        self.queue  = []
    
    def do_bfs(self, start_node_idx):
        key = start_node_idx
        self.queue.append(key)
        self.visited.append(key)

        print("BFS of the graph:")
        while self.queue:
            current_node_idx = self.queue.pop(0)
            print(self.graph[current_node_idx].name, " ")
        
            for child in self.graph[current_node_idx].children:
                child_idx = child.id
                if child_idx not in self.visited:
                    self.visited.append(child_idx)
                    self.queue.append(child_idx)

                
            
        

