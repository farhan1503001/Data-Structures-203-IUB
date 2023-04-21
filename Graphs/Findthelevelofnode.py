from Graph import Graph
def find_distance_nodes(graph,source):
    #Create a visited dictionary
    visited=dict()
    q=[]
    q.append(source)
    q.append('END')
    visited[source]=True
    level=0
    print(f'{[q[0]]} have all distance {level} from source{source}')
    while len(q)>1:
        temp=q.pop(0)
        if temp=="END":
            level=level+1
            print(f'{q} have all distance{level} from source{source}')
            q.append('END')
            continue
        else:
            for node in graph.graph[temp]:
                if node not in visited:
                    q.append(node)
                    visited[node]=True
                else:
                    pass
if __name__=="__main__":
    graph=Graph()
    graph.add_edge(1,3)
    graph.add_edge(3,1)
    graph.add_edge(0,1)
    graph.add_edge(1,0)
    graph.add_edge(1,2)
    graph.add_edge(2,3)
    graph.add_edge(3,1)

    graph.print_graph()

    find_distance_nodes(graph,0)

        

        
