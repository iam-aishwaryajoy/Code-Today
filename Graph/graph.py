import graphviz
import string
import random
import numpy as np
from bfs import *

class Graph:
    def __init__(self):
        self.graph = {}
        self.nodes = []
        self.idx_list = []
        self.key = -1
    
    def create_graph(self, nodes):
        for ids, name in nodes.items():
            #self.key = self.key + 1
            self.key = ids
            self.idx_list.append(self.key)
            node = self.Node(self.key, name)
            self.nodes.append(node)
            self.graph[self.key] = node
        #print(self.graph)
    def delete_val(self, stack, value):
        if value in stack:
           stack.remove(value)
        return stack
        
    def create_graph_automatically(self, node_length):
        choice = string.ascii_uppercase
        for key in range(node_length):
            name = random.choice(choice)
            choice = choice.split()
            choice = self.delete_val(choice, name)
            choice = ''.join(str(e) for e in choice)
            self.key = key
            self.idx_list.append(self.key)
            node = self.Node(self.key, name)
            self.nodes.append(node)
            self.graph[self.key] = node

    def find_random_value(self, node_length):
        return random.randint(0, node_length)

            
    def create_links_automatically(self, node_length, self_loop=False):
        visited = {}
        for n in range(node_length):
            visited[n] = 0
        parent_stack = np.arange((node_length))
        parent_stack = parent_stack.tolist()
        child_stack = np.arange((node_length))
        child_stack = child_stack.tolist()
        print('Parent stack:', parent_stack)
        print('Child stack:', child_stack)
        links = node_length*2
        for link in range(links):
            parent = random.choice(parent_stack)
            if visited[parent] < 2:
                visited[parent] = visited[parent] + 1
                child_stack = self.delete_val(child_stack, parent)
                for ch in self.graph[parent].children:
                    child_stack = self.delete_val(child_stack, ch)
                child = random.choice(child_stack)
            else:
                parent_stack = self.delete_val(parent_stack, parent)
                break
            print('Parent stack:', parent_stack)
            print('Child stack:', child_stack)
            self.add_child(parent,child)


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
    #graph.create_graph({0:'A',1:'B',2:'C',3:'D',4:'E',5:'F'})

    graph.create_graph_automatically(node_length=6)
    #graph.add_child(0,1)
    #graph.add_child(0,2)
    #graph.add_child(2,4)
    #graph.add_child(1,3)
    #graph.add_child(3,5)
    #graph.add_child(6,4)
    graph.create_links_automatically(node_length=6, self_loop=False)
    bfs = BFS(graph.graph)
    bfs.do_bfs(0)
    graph.print_graph()


