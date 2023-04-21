from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.graph=defaultdict(list)
    def add_edge(self,u,v):
        self.graph[u].append(v)
    def print_graph(self):
        print(self.graph)

    def __len__(self):
        return len(self.graph)

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
    print(graph.__len__())