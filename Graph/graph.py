from bfs import *
from import_library import *
from node import *


class Graph:
    def __init__(self):
        self.graph = {}
        self.nodes = []
        self.idx_list = []
        self.key = -1
    
    def create_graph(self, nodes):
        for ids, name in nodes.items():
            self.key = ids
            self.idx_list.append(self.key)
            node = Node(self.key, name)
            self.nodes.append(node)
            self.graph[self.key] = node
    
    def delete_val(self, stack, value):
        if value in stack:
           stack.remove(value)
        return stack
        
    def create_graph_automatically(self, node_length):
        choice = string.ascii_uppercase
        for key in range(node_length):
            name = random.choice(choice)
            choice = [*choice]
            #log.debug("Choice:{}".format(choice))
            choice = self.delete_val(choice, name)
            #log.debug("Choice:{}".format(choice))
            choice = ''.join(str(e) for e in choice)
            self.key = key
            self.idx_list.append(self.key)
            node = Node(self.key, name)
            self.nodes.append(node)
            self.graph[self.key] = node
            #log.debug("Key:{}, Name:{}, Choice:{}".format(key, name, choice))

    def find_random_value(self, node_length):
        return random.randint(0, node_length)

    def handle_single_nodes(self, node_length):
        for key, node in self.graph.items():
            parent_stack = np.arange((node_length))
            parent_stack = parent_stack.tolist()
            if not node.parents and not node.children:
                parent_stack = self.delete_val(parent_stack, key)
                parent = random.choice(parent_stack)
                log.debug(" Key: {}, Parent stack:{}, parents:{}, children:{}, Name:{}".format(key, parent_stack, node.parents, node.children, node.name))
                self.add_child(parent, key)
                log.debug("CHILD:{}, PARENT:{}".format(self.graph[key].name,self.graph[parent].name))
                
    def create_links_automatically(self, node_length, self_loop=False):
        visited = {}
        for n in range(node_length):
            visited[n] = 0
        parent_stack = np.arange((node_length))
        parent_stack = parent_stack.tolist()
        log.debug(' Initial Parent stack:{}'.format(parent_stack))
        links = (node_length*2)
        for link in range(links):
            parent = random.choice(parent_stack)
            child_stack = np.arange((node_length))
            child_stack = child_stack.tolist()
            log.debug(' Initial child stack:{}'.format(child_stack))
            if visited[parent] < 2:
                visited[parent] = visited[parent] + 1
                child_stack = self.delete_val(child_stack, parent)
                log.debug(' Child stack after deleting parent:{}'.format(child_stack))
                for ch in self.graph[parent].children:
                    child_stack = self.delete_val(child_stack, ch.id)
                    log.debug(' Child stack after deleting children:{}'.format(child_stack))
                child = random.choice(child_stack)
            else:
                parent_stack = self.delete_val(parent_stack, parent)
                break
            log.debug(" PARENT:{}, CHILD:{}".format(self.graph[parent].name, self.graph[child].name))
            self.add_child(parent,child)
        self.handle_single_nodes(node_length)


    def add_child(self, parent_key, child_key):
        if parent_key in self.idx_list and child_key in self.idx_list:        
            self.nodes[parent_key].children.append(self.nodes[child_key])
            self.nodes[child_key].parents.append(self.nodes[parent_key])
        else:
            print("The keys", parent_key, "or" ,child_key, "are not available")

    def print_graph(self):
        dot = graphviz.Digraph()
        for key, parent in self.graph.items():
            dot.node(parent.name)
        for key, parent in self.graph.items():
            for child in parent.children:
                dot.edge(parent.name, child.name)
        print(dot.source)
        dot.render(directory='results', view=True, format='jpg')

    def find_root_node(self):
        for key,val in self.graph.items():
            if not val.parents and len(val.children)>1:
                return key
        for key,val in self.graph.items():
            if not val.parents:
                return key
            
        for key,val in self.graph.items():
            if not val.parents and len(val.children)>0:
                return key
        for key,val in self.graph.items():
            return key

    def print_g(self):
        for key, val in self.graph.items():
            print(key, val.name)

