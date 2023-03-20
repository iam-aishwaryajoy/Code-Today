class Graph:
    def __init__(self):
        self.graph = {}
        self.nodes = []
        self.key = -1
    
    def create_graph(self, nodes):
        for node in nodes:
            self.key = self.key + 1
            node = self.Node(node)
            self.nodes.append(node)
            self.graph[self.key] = node
        #print(self.graph)
        
    def add_child(self, parent_key, child_key):
        self.nodes[parent_key].children.append(self.nodes[child_key])

    def print_graph(self):
        print("Nodes are:")
        for key, parent in self.graph.items():
            print(parent.value)
        print("Connections are:")
        for key, parent in self.graph.items():
            for child in parent.children:
                print(parent.value, "->", child.value)
    class Node:
        def __init__(self, value):
            self.value = value
            self.children = []





    

graph = Graph()
graph.create_graph(['A','B','C','D'])
graph.add_child(0,3)
graph.add_child(1,2)
graph.print_graph()

            
            
            
