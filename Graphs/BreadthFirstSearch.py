from Graph import Graph

def BFS(graph,source):
    """
    input parameters will be source node and graph

    return minimum path from the source nodes
    """
    #A map or dictionary for tracking which nodes has been visited
    visited=dict()
    #Denoting a queue at first just like bfs
    q=[]
    #pushing source just like bst
    q.append(source)
    #Make source node visited
    visited[source]=True
    
    while len(q)!=0:
        temp=q.pop(0)
        #pop the first value
        print(temp,end="->")
        #Now push all the unvisited node of temp to q
        for node in graph.graph[temp]:
            if node not in visited:
                visited[node]=True
                q.append(node)
            else:
                pass


if __name__=="__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    BFS(g,0)
