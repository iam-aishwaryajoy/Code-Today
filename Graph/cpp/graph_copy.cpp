#include<iostream>
#include<list>
#include<map>
using namespace std;

class Graph{
    public:
        map<int, bool> bfs_visited;
        map<int, bool> visited;
        map<int, list<int>> adj;
        list<int> dfs_lists;
        list<int> bfs_lists;

        void add_edge(int v, int w);
        void DFS(int v);
        void BFS(int v);
};

void Graph::add_edge(int v, int w){
    adj[v].push_back(w);
}

void Graph::DFS(int v){
    visited[v] = true;

    dfs_lists.push_back(v);
    //list<int>::iterator i;
    //for (i=adj[v].begin(); i!=adj[v].end(); i++){
        //if (!visited[*i])
        //DFS(*i);
    //}
    for(auto i:adj[v]){
        if(!visited[i])
        DFS(i);}
}
void Graph::BFS(int v){
    bfs_visited[v] = true;
    list<int>queue;
    queue.push_back(v);
    
    while(!queue.empty()){
        v = queue.front();
        bfs_lists.push_back(v);
        queue.pop_front();
        for (auto adjacent : adj[v]) {                                    if (!bfs_visited[adjacent]){
                bfs_visited[adjacent] = true;                                     queue.push_back(adjacent);}
         }
    }
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

    cout << "Following is Depth First Traversal"
            " (starting from vertex 2) \n";
    //g.DFS(2);
    //for(auto i:g.dfs_lists){cout<<i;}
    
    g.BFS(2);
    for(auto i:g.bfs_lists){cout<<i;}
    
    return 0;
}
