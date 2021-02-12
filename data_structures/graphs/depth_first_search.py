from graph import Graph

class DepthFirstSearch:
    def __init__(self, G: Graph, s: int):
        '''
        Simple DFS using recursion
        Given a graph and a node,
        recursivly visit each node 
        connected to the given node, marking the 
        ones we visit in marked[]
        '''
        self.graph = G
        self.s = s
        self.marked = [False] * self.graph.print_vertices()
        self.dfs(self.graph, self.s)

    def dfs(self, g: Graph, v: int):
        print(v)
        self.marked[v] = True
        for w in g.adj_list[v]:
            if not self.marked[w]:
                self.dfs(g, w)

