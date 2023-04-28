#include<iostream>
#include<list>
#include<map>
using namespace std;
struct Node{
    int id;
    int child;
    Node* next;
};
class Graph{
    public:
        head = new Node*[4]();
        this->sizes = 4;
        for (int i = 0; i < N; i++){
        head[i] = nullptr;}
        void add_edge(int v, int w);
};

void Graph::add_edge(int v, int w){
    adj[v].push_back(w);
    *Node node = new node;
    node->id = v;
    node->child = w;
    node->next = head;
}

int main()
{
    Graph g;
    g.add_edge(0, 1);
    g.add_edge(0, 2);
    g.add_edge(1, 2);
    g.add_edge(2, 0);
    g.add_edge(2, 3);
    g.add_edge(3, 3);
    
    
    return 0;
}
