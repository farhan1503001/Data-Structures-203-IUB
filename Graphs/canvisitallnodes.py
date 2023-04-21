from Graph import Graph

def can_visit_nodes(graph,source):
    visited=dict()

    q=[]
    visited[source]=True
    q.append(source)

    count=0
    while len(q)!=0:
        temp=q.pop(0)
        count=count+1
        for node in graph.graph[temp]:
            if node not in visited:
                visited[node]=True
                q.append(node)
            else:
                pass
    return count==graph.__len__()

if __name__=="__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print(can_visit_nodes(g,0))

        

