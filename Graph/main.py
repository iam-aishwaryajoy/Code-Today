from graph import *

if __name__ == "__main__":
    graph = Graph()
    log.basicConfig(filename='Graph.log', level=log.DEBUG)
    #graph.create_graph({0:'A',1:'B',2:'C',3:'D',4:'E',5:'F'})

    graph.create_graph_automatically(node_length=6)
    #graph.add_child(0,1)
    #graph.add_child(0,2)
    #graph.add_child(2,4)
    #graph.add_child(1,3)
    #graph.add_child(3,5)
    #graph.add_child(6,4)
    graph.create_links_automatically(node_length=6, self_loop=False)
    graph.print_g()
    bfs = BFS(graph.graph)
    root_node = graph.find_root_node()
    bfs.do_bfs(root_node)
    graph.print_graph()
