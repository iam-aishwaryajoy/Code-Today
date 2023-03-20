import graphviz 

class Graph:
    def __init__(self):
        self.graph = {}
        self.nodes = []
        self.idx_list = []
        self.key = -1
    
    def create_graph(self, nodes):
        for name in nodes:
            self.key = self.key + 1
            self.idx_list.append(self.key)
            node = self.Node(self.key, name)
            self.nodes.append(node)
            self.graph[self.key] = node
        #print(self.graph)
        
    def add_child(self, parent_key, child_key):
        if parent_key in self.idx_list and child_key in self.idx_list:        
            self.nodes[parent_key].children.append(self.nodes[child_key])
        else:
            print("The keys", parent_key, " " ,child_key, "are not available")

    def print_graph(self):
        dot = graphviz.Digraph()
        for key, parent in self.graph.items():
            dot.node(parent.name)
        for key, parent in self.graph.items():
            for child in parent.children:
                #print(parent.name, "->", child.name)
                dot.edge(parent.name, child.name)
        print(dot.source)
        dot.render(directory='results', view=True, format='jpg')

    class Node:
        def __init__(self, ids, name):
            self.id = ids
            self.name = name
            self.children = []


if __name__ == "__main__":
    graph = Graph()
    graph.create_graph(['A','B','C','D','E','F'])
    graph.add_child(0,3)
    graph.add_child(1,2)
    graph.add_child(3,1)
    graph.add_child(5,1)
    graph.add_child(4,5)
    graph.add_child(6,4)

    graph.print_graph()

